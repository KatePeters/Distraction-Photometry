# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:14:15 2017

@author: kp259
"""

# THPH Photometry analysis 

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import seaborn as sb

sb.set_context("paper")
sb.set_style("white")

# Plot settings, font / size / stylesd
Calibri = {'fontname':'Calibri'}
Size = {'fontsize': 20}
label_size = 14
plt.rcParams['xtick.labelsize'] = label_size 
plt.rcParams['ytick.labelsize'] = label_size 


def asnumeric(s):
    try:
        x = float(s)
        return x
    except ValueError:
        return float('nan')

def medfilereader(filename, varsToExtract = 'all',
                  sessionToExtract = 1,
                  verbose = False,
                  remove_var_header = False):
    if varsToExtract == 'all':
        numVarsToExtract = np.arange(0,26)
    else:
        numVarsToExtract = [ord(x)-97 for x in varsToExtract]
    
    f = open(filename, 'r')
    f.seek(0)
    filerows = f.readlines()[8:]
    datarows = [asnumeric(x) for x in filerows]
    matches = [i for i,x in enumerate(datarows) if x == 0.3]
    if sessionToExtract > len(matches):
        print('Session ' + str(sessionToExtract) + ' does not exist.')
    if verbose == True:
        print('There are ' + str(len(matches)) + ' sessions in ' + filename)
        print('Analyzing session ' + str(sessionToExtract))
    
    varstart = matches[sessionToExtract - 1]
    medvars = [[] for n in range(26)]
    
    k = int(varstart + 27)
    for i in range(26):
        medvarsN = int(datarows[varstart + i + 1])
        
        medvars[i] = datarows[k:k + int(medvarsN)]
        k = k + medvarsN
        
    if remove_var_header == True:
        varsToReturn = [medvars[i][1:] for i in numVarsToExtract]
    else:
        varsToReturn = [medvars[i] for i in numVarsToExtract]

    if np.shape(varsToReturn)[0] == 1:
        varsToReturn = varsToReturn[0]
    return varsToReturn


def MetaExtractor (metafile):
    f = open(metafile, 'r')
    f.seek(0)
    Metafilerows = f.readlines()[1:]
    tablerows = []

    for row in Metafilerows: 
        items = row.split(',')
        tablerows.append(items)

    MedFilenames, RatID, Date, Day, Session, Drug, TotLicks, Distractions, \
    NonDistractions, PercentDistracted = [], [], [], [], [], [], [], [], [], []

    for i, lst in enumerate(tablerows):
       MedFilenames = MedFilenames + [lst[1]]
       RatID = RatID + [lst[2]]
       Date = Date + [lst[3]]
       #Day = Day + [lst[3]]
       Session = Session + [lst[4]]
     #  Drug = Drug + [lst[5]]
       TotLicks = TotLicks + [lst[6]]
       Distractions = Distractions + [lst[8]] 
       #NonDistractions = NonDistractions + [lst[8]]
       PercentDistracted = PercentDistracted + [lst[9]]
 
    return ({'MedFilenames':MedFilenames, 'RatID':RatID, 'Date':Date, 'Session':Session, \
             'TotLicks':TotLicks, 'Distractions':Distractions, \
             'PercentDistracted':PercentDistracted})
    
def remcheck(val, range1, range2):
    # function checks whether value is within range of two decimels
    if (range1 < range2):
        if (val > range1) and (val < range2):
            return True
        else:
            return False
    else:
        if (val > range1) or (val < range2):
            return True
        else:
            return False

def distractionCalc2(licks, pre=1, post=1):
    licks = np.insert(licks, 0, 0)
    b = 0.001
    d = []
    idx = 3
    
    while idx < len(licks):
        if licks[idx]-licks[idx-2] < 1 and remcheck(b, licks[idx-2] % 1, licks[idx] % 1) == False:
                d.append(licks[idx])
                b = licks[idx] % 1
                idx += 1
                try:
                    while licks[idx]-licks[idx-1] < 1:
                        b = licks[idx] % 1
                        idx += 1
                except IndexError:
                    pass
        else:
            idx +=1
    
    return d

 

def distractedOrNot(distractors, licks):
    distracted = []
    notdistracted = []
    lickList = []
    for l in licks:
        lickList.append(l)
    
    
    
    for index, distractor in enumerate(distractors):
        if distractor in licks:

            ind = lickList.index(distractor)
 
            if (licks[ind+1] - licks[ind]) > 1:
                distracted.append(licks[ind])
            else:
                if (licks[ind+1] - licks[ind]) < 1:
                    notdistracted.append(licks[ind])
        

    return(distracted, notdistracted)



def loadmatfile(file):
    a = sio.loadmat(file, squeeze_me=True, struct_as_record=False)
    
    sessiondict = {}
    sessiondict['blue'] = a['output'].blue
    sessiondict['uv'] = a['output'].uv
    sessiondict['fs'] = a['output'].fs   
    sessiondict['licks'] = a['output'].licks.onset

    sessiondict['distractors'] = distractionCalc2(sessiondict['licks'])

#   #write distracted or not to produce 2 lists of times, distracted and notdistracted
    #distracted, notdistracted= distractedOrNot(sessiondict['distractors'], sessiondict['licks'])
#    
    sessiondict['distracted'], sessiondict['notdistracted'] = distractedOrNot(sessiondict['distractors'], sessiondict['licks'])
   # sessiondict['notdistracted'] = notdistracted
    
    return sessiondict

def time2samples(self):
    tick = self.output.Tick.onset
    maxsamples = len(tick)*int(self.fs)
    if (len(self.data) - maxsamples) > 2*int(self.fs):
        print('Something may be wrong with conversion from time to samples')
        print(str(len(self.data) - maxsamples) + ' samples left over. This is more than double fs.')
    
    self.t2sMap = np.linspace(min(tick), max(tick), maxsamples)
    
def snipper(data, timelock, fs = 1, t2sMap = [], preTrial=10, trialLength=30,
                 adjustBaseline = True,
                 bins = 0):

    if len(timelock) == 0:
        print('No events to analyse! Quitting function.')
        raise Exception('no events')
    nSnips = len(timelock)
    pps = int(fs) # points per sample
    pre = int(preTrial*pps) 
#    preABS = preTrial
    length = int(trialLength*pps)
# converts events into sample numbers
    event=[]
    if len(t2sMap) > 1:
        for x in timelock:
            event.append(np.searchsorted(t2sMap, x, side="left"))
    else:
        event = [x*fs for x in timelock]

    avgBaseline = []
    snips = np.empty([nSnips,length])

    for i, x in enumerate(event):
        start = int(x) - pre
        avgBaseline.append(np.mean(data[start : start + pre]))
#        print(x)
        try:
            snips[i] = data[start : start+length]
        except ValueError: # Deals with recording arrays that do not have a full final trial
            snips = snips[:-1]
            avgBaseline = avgBaseline[:-1]
            nSnips = nSnips-1

    if adjustBaseline == True:
        snips = np.subtract(snips.transpose(), avgBaseline).transpose()
        snips = np.divide(snips.transpose(), avgBaseline).transpose()

    if bins > 0:
        if length % bins != 0:
            snips = snips[:,:-(length % bins)]
        totaltime = snips.shape[1] / int(fs)
        snips = np.mean(snips.reshape(nSnips,bins,-1), axis=2)
        pps = bins/totaltime
              
    return snips, pps

def trialsFig(ax, trials1, trials2, pps=1, preTrial=10, scale=5, noiseindex = [],
              plotnoise=True,
              eventText='event', 
              ylabel=''):

    if len(noiseindex) > 0:
        trialsNoise = np.array([i for (i,v) in zip(trials1, noiseindex) if v])
        trials1 = np.array([i for (i,v) in zip(trials1, noiseindex) if not v])
        if plotnoise == True:
            ax.plot(trialsNoise.transpose(), c='red', alpha=0.4)
        
    ax.plot(trials1.transpose(), c='lightblue', alpha=0.6)
    
    
    ax.plot(trials2.transpose(), c='thistle', alpha=0.6)
    ax.plot(np.mean(trials2, axis=0), c='purple', linewidth=2)
    ax.plot(np.mean(trials1,axis=0), c='blue', linewidth=2)
    ax.set(ylabel = ylabel)
    ax.xaxis.set_visible(False)
            
    scalebar = scale * pps

    yrange = ax.get_ylim()[1] - ax.get_ylim()[0]
    scalebary = (yrange / 10) + ax.get_ylim()[0]
    scalebarx = [ax.get_xlim()[1] - scalebar, ax.get_xlim()[1]]
    
    ax.plot(scalebarx, [scalebary, scalebary], c='k', linewidth=2)
    ax.text((scalebarx[0] + (scalebar/2)), scalebary-(yrange/50), str(scale) +' s', ha='center',va='top', **Calibri, **Size)
 
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    xevent = pps * preTrial  
    ax.plot([xevent, xevent],[ax.get_ylim()[0], ax.get_ylim()[1] - yrange/20],'--')
    ax.text(xevent, ax.get_ylim()[1], eventText, ha='center',va='bottom', **Calibri, **Size)
    
    return ax

# sort out looping, meta extract etc.

#THPH1
#THPH2
datafolder = 'R:/DA_and_Reward/Shared/Scripts/Matlab Files/'

datafile = datafolder + 'thph2.1distraction.mat' 

examplerat = loadmatfile(datafile)


blueSnips, ppsBlue = snipper(examplerat['blue'], examplerat['distractors'], fs=examplerat['fs'], bins=300)
uvSnips, ppsUV = snipper(examplerat['uv'], examplerat['distractors'], fs=examplerat['fs'], bins=300)

fig1 = plt.figure()
ax1 = plt.subplot(1,1,1)
ax1.set_ylim([-0.01, 0.01])
trialsFig(ax1, blueSnips, uvSnips, ppsBlue)



#
#
#def med_abs_dev(data, b=1.4826):
#    median = np.median(data)
#    devs = [abs(i-median) for i in data]
#    mad = np.median(devs)*b
#                   
#    return mad
#
#def findnoise(data, background, t2sMap = [], fs = 1, bins=0, method='sd'):
#    
#    bgSnips, _ = snipper(data, background, t2sMap=t2sMap, fs=fs, bins=bins)
#    
#    if method == 'sum':
#        bgSum = [np.sum(abs(i)) for i in bgSnips]
#        bgMAD = med_abs_dev(bgSum)
#    elif method == 'sd':
#        bgSD = [np.std(i) for i in bgSnips]
#        bgMAD = med_abs_dev(bgSD)
#   
#    return(bgMAD)
#
#
#def makerandomevents(minTime, maxTime, spacing = 77, n=100):
#    events = []
#    total = maxTime-minTime
#    start = 0
#    for i in np.arange(0,n):
#        if start > total:
#            start = start - total
#        events.append(start)
#        start = start + spacing
#    events = [i+minTime for i in events]
#    return events
#
#
#def makephotoTrials(self, bins, events, threshold=10):
#    bgMAD = jmf.findnoise(self.data, self.randomevents,
#                          t2sMap = self.t2sMap, fs = self.fs, bins=bins,
#                          method='sum')          
#    blueTrials, self.pps = jmf.snipper(self.data, events,
#                                        t2sMap = self.t2sMap, fs = self.fs, bins=bins)        
#    UVTrials, self.pps = jmf.snipper(self.dataUV, events,
#                                        t2sMap = self.t2sMap, fs = self.fs, bins=bins)
#    sigSum = [np.sum(abs(i)) for i in blueTrials]
#    sigSD = [np.std(i) for i in blueTrials]
#    noiseindex = [i > bgMAD*threshold for i in sigSum]
#
#    return blueTrials, UVTrials, noiseindex
#
#
#
#def removenoise(snipsIn, noiseindex):
#    snipsOut = np.array([x for (x,v) in zip(snipsIn, noiseindex) if not v])   
#    return snipsOut
#
#
#
#
#
#
#foundnoise1 = findnoise(examplerat['blue1'], examplerat['distractors1'], fs=examplerat['fs1'])
#randevents1 = makerandomevents(examplerat['blue1'][100], examplerat['blue1'][-100])
#threshold1 = 1000
#sigSum1 = [np.sum(abs(i)) for i in blueSnips1]
#sigSD1 = [np.std(i) for i in blueSnips1]
#noiseindex1 = [i > foundnoise1*threshold1 for i in sigSum1]
#
#blueRemNoise1 = removenoise(blueSnips1, noiseindex1)
#uvRemNoise1 = removenoise(uvSnips1, noiseindex1)
#
#
#fig3 = plt.figure()
#ax3 = plt.subplot(1,1,1)
#ax3.set_ylim([-0.02, 0.02])
#trialsFig(ax3, blueRemNoise1, uvRemNoise1, pps1, eventText='distractor')
#
#
## Statistics, make array of maximums 
#blueMeans1 = np.mean(blueRemNoise1, axis=0)
#blueMeans5sec1 = blueMeans1[100:150]
#e1 = max(blueMeans5sec1)
#
#uvMeans1 = np.mean(uvRemNoise1, axis=0)
#uvMenas5sec1 = uvMeans1[100:150]
#g1 = max(uvMenas5sec1)
#
#print(e1,g1)
#
#
#
##BOX 2
#
#foundnoise2 = findnoise(examplerat['blue2'], examplerat['distractors2'], fs=examplerat['fs2'])
#randevents2 = makerandomevents(examplerat['blue2'][100], examplerat['blue2'][-100])
#threshold2 = 800
#
#sigSum2 = [np.sum(abs(i)) for i in blueSnips2]
#sigSD12= [np.std(i) for i in blueSnips2]
#noiseindex2 = [i > foundnoise2*threshold2 for i in sigSum2]
#
#blueRemNoise2 = removenoise(blueSnips2, noiseindex2)
#uvRemNoise2 = removenoise(uvSnips2, noiseindex2)
#
#
#fig4 = plt.figure()
#ax4 = plt.subplot(1,1,1)
#ax4.set_ylim([-0.075, 0.075])
#trialsFig(ax4, blueRemNoise2, uvRemNoise2, pps2, eventText='distractor')
#
#
##Statistics, make array of maximums 
#blueMeans2 = np.mean(blueRemNoise2, axis=0)
#blueMeans5sec2 = blueMeans2[100:150]
#e2 = max(blueMeans5sec2)
#
#uvMeans2 = np.mean(uvRemNoise2, axis=0)
#uvMenas5sec2 = uvMeans2[100:150]
#g2 = max(uvMenas5sec2)
#
#print(e2,g2)
#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Massively overcomplicated method to make mean plots
## Added individual lines to the plot (could have used Trial figs)
#
#meansfile = 'D:/Third year report/Photometry figs/MaxPeaksLick.csv'
#
#f = open(meansfile, 'r')
#f.seek(0)
#filerows = f.readlines()[1:]
#tablerows2 = []
#
#for row in filerows: 
#    items = row.split(',')
#    tablerows2.append(items)
#
#b21, b22, b23, b24, b25, b26, BM, u21, u22, u23, u24, u25, u26, UM = [], \
#[], [], [], [], [], [], [], [], [], [], [], [], []
#
#for i, lst in enumerate(tablerows2):
#   
#    b21 = b21 + [lst[0]]
#    b22 = b22 + [lst[1]]
#    b23 = b23 + [lst[2]]
#    b24 = b24 + [lst[3]]
#    b25 = b25 + [lst[4]]
#    b26 = b26 + [lst[5]]
#    BM = BM + [lst[6]]
#    u21 = u21 + [lst[7]]
#    u22 = u22 + [lst[8]]
#    u23 = u23 + [lst[9]]
#    u24 = u24 + [lst[10]]
#    #u25 = u25 + [lst[11]]
#    u26 = u26 + [lst[11]]
#    UM = UM + [lst[12]]
#
##'2.5b':b25
#allMeans = {'2.1b':b21, '2.2b':b22, '2.3b':b23, '2.4b':b24, '2.6b':b26,\
#            'BlueMeanAll': BM, '2.1u':u21, '2.2u':u22, '2.3u':u23, '2.4u':u24, '2.5u':u25,\
#            '2.6u':u26, 'UVMeanAll':UM}
#
#fig5 = plt.figure()
#ax5 = plt.subplot(1,1,1)
#ax5.set_ylim([-0.04, 0.04])
#
#    
#scale = 5
#eventText='distractor' 
#ylabel=''   
#pps = pps2 # note this is retrieved from previous code 
#preTrial = 10
#
#ax5.plot(np.asarray(allMeans['2.1b']).transpose(), c='lightblue', alpha=0.6)
#ax5.plot(np.asarray(allMeans['2.2b']).transpose(), c='lightblue', alpha=0.6)
#ax5.plot(np.asarray(allMeans['2.3b']).transpose(), c='lightblue', alpha=0.6)
#ax5.plot(np.asarray(allMeans['2.4b']).transpose(), c='lightblue', alpha=0.6)
##ax5.plot(np.asarray(allMeans['2.5b']).transpose(), c='lightblue', alpha=0.6)
#ax5.plot(np.asarray(allMeans['2.6b']).transpose(), c='lightblue', alpha=0.6)
#
#ax5.plot(np.asarray(allMeans['2.1u']).transpose(), c='thistle', alpha=0.6)
#ax5.plot(np.asarray(allMeans['2.2u']).transpose(), c='thistle', alpha=0.6)
#ax5.plot(np.asarray(allMeans['2.3u']).transpose(), c='thistle', alpha=0.6)
#ax5.plot(np.asarray(allMeans['2.4u']).transpose(), c='thistle', alpha=0.6)
#ax5.plot(np.asarray(allMeans['2.5u']).transpose(), c='thistle', alpha=0.6)
#ax5.plot(np.asarray(allMeans['2.6u']).transpose(), c='thistle', alpha=0.6)
#
#ax5.plot(np.asarray(allMeans['BlueMeanAll']).transpose(), c='blue', alpha=1)
#ax5.plot(np.asarray(allMeans['UVMeanAll']).transpose(), c='purple', alpha=1)
#
#ax5.set(ylabel = ylabel)
#ax5.xaxis.set_visible(False)
#        
#scalebar = scale * pps
#
#yrange = ax5.get_ylim()[1] - ax5.get_ylim()[0]
#scalebary = (yrange / 10) + ax5.get_ylim()[0]
#scalebarx = [ax5.get_xlim()[1] - scalebar, ax5.get_xlim()[1]]
#
#ax5.plot(scalebarx, [scalebary, scalebary], c='k', linewidth=2)
#ax5.text((scalebarx[0] + (scalebar/2)), scalebary-(yrange/50), str(scale) +' s', ha='center',va='top', **Calibri, **Size)
# 
#ax5.spines['right'].set_visible(False)
#ax5.spines['top'].set_visible(False)
#ax5.spines['bottom'].set_visible(False)
#
#xevent = pps * preTrial  
#ax5.plot([xevent, xevent],[ax5.get_ylim()[0], ax5.get_ylim()[1] - yrange/20],'--')
#ax5.text(xevent, ax5.get_ylim()[1], eventText, ha='center',va='bottom', **Calibri, **Size)
