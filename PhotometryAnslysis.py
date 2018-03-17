# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:14:15 2017

@author: kp259
"""

# THPH Photometry analysis 


# Plot settings, font / size / stylesd
#Calibri = {'fontname':'Calibri'}
#Size = {'fontsize': 20}
#label_size = 14
#plt.rcParams['xtick.labelsize'] = label_size 
#plt.rcParams['ytick.labelsize'] = label_size 

from AllFunctions import *

datafolder = '/Volumes/KPMSB352/PHOTOMETRY MMIN18/'
#datafolder = 'F:\\PHOTOMETRY MMIN18\\'

datafile = datafolder + 'thph2.6lick3.mat' 
#datafile = datafolder + 'thph2.6distraction.mat'
datafile = datafolder + 'thph2.3distraction.mat' #trial 17, 8 
#datafile = datafolder + 'thph2.5distraction.mat' # trial 5
examplerat = loadmatfile(datafile)

print(examplerat['licks'][-1])

blueSnips, ppsBlue = snipper(examplerat['blue'], examplerat['notdistracted'], fs=examplerat['fs'], bins=300)
uvSnips, ppsUV = snipper(examplerat['uv'], examplerat['notdistracted'], fs=examplerat['fs'], bins=300)

#fig1 = plt.figure()
#ax1 = plt.subplot(1,1,1)
#ax1.set_ylim([-0.01, 0.01])
#trialsFig(ax1, blueSnips, uvSnips, ppsBlue)

randevents = makerandomevents(examplerat['blue'][300], examplerat['blue'][-300])
bgMad, bgMean = findnoise(examplerat['blue'], randevents, fs=examplerat['fs'], method='sum', bins=300)
threshold = 1
sigSum = [np.sum(abs(i)) for i in blueSnips]


#sigSD = [np.std(i) for i in blueSnips]
noiseindex = [i > bgMean + bgMad*threshold for i in sigSum]
print(noiseindex)
#
#blueRemNoise = removenoise(blueSnips, noiseindex)
#uvRemNoise = removenoise(uvSnips, noiseindex)
#

''' Longer timecourse - code doesn't work yet '''

#longSnipsB, ppsBlue = snipper(examplerat['blue'], examplerat['notdistracted'], fs=examplerat['fs'], bins=300)
#longSnipsUV, ppsUV = snipper(examplerat['uv'], examplerat['notdistracted'], fs=examplerat['fs'], bins=300)
#trialsFig(ax3,longSnipsB, longSnipsUV, ppsBlue)

#
fig3 = plt.figure()
ax3 = plt.subplot(1,1,1)
#ax3.set_ylim([-0.2, 0.2])
trialsFig(ax3, blueSnips, uvSnips, ppsBlue, eventText='distractor', noiseindex=noiseindex) #, )






fig4 = plt.figure()
ax4 = plt.subplot(1,1,1)
ax4.set_ylim([-0.05, 0.05])


trialsMultShadedFig(ax4, [uvSnips,blueSnips], ppsBlue, eventText='distractor')


# Statistics, make array of maximums 
blueMeans = np.mean(blueSnips, axis=0)
blueMeans2sec = blueMeans[100:120]
e1 = max(blueMeans2sec)

uvMeans = np.mean(uvSnips, axis=0)
uvMenas2sec = uvMeans[100:120]
g1 = max(uvMenas2sec)

print(e1,g1)


# Can I get it to store all the blue snips as columns in excel?
# Then access these?
# For now manual 
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Massively overcomplicated method to make mean plots
## Added individual lines to the plot (could have used Trial figs but data type issue)
# Snips means 
#(1) Peaks on licking, modelled distractors means (not alligned to lick event though - do this)
#(2) Peaks for real distractors
#(3) Peaks distracted
#(4) Peaks not distracted
#(5) Peaks alligned to first lick 

#meansfile = '/Volumes/KPMSB352/PHOTOMETRY MMIN18/Snips means lickmodel.csv'
#meansfile = 'D:/PHOTOMETRY MMIN18/Snips means distractors.csv'
meansfile = '/Volumes/KPMSB352/PHOTOMETRY MMIN18/Snips means notdistracted2.csv'
#meansfile = 'F:\\PHOTOMETRY MMIN18\\Snips means distracted.csv'
#meansfile = 'D:/PHOTOMETRY MMIN18/Snips means notdistracted.csv'
#meansfile = '/Volumes/KPMSB352/PHOTOMETRY MMIN18/Snips means lickalligned.csv'



f = open(meansfile, 'r')
f.seek(0)
filerows = f.readlines()[1:]
tablerows2 = []

for row in filerows: 
    items = row.split(',')
    tablerows2.append(items)

b11, b12, b13, b14, b15, b16, b21, b22, b23, b24, b25, b26, b27, b28, BLUEMEAN, \
u11, u12, u13, u14, u15, u16, u21, u22, u23, u24, u25, u26, u27, u28, UVMEAN = [], \
[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], \
[], [], [], [], [], [], [], [], []

for i, lst in enumerate(tablerows2):
    b11 = b11 + [lst[0]]
    b12 = b12 + [lst[1]]
    b13 = b13 + [lst[2]]
    b14 = b14 + [lst[3]]
    b15 = b15 + [lst[4]]
    b16 = b16 + [lst[5]]
    b21 = b21 + [lst[6]]
    b22 = b22 + [lst[7]]
    b23 = b23 + [lst[8]]
    b24 = b24 + [lst[9]]
    b25 = b25 + [lst[10]]
    b26 = b26 + [lst[11]]
    b27 = b27 + [lst[12]]
    b28 = b28 + [lst[13]]
    BLUEMEAN = BLUEMEAN + [lst[14]]
    u11 = u11 + [lst[15]]
    u12 = u12 + [lst[16]]
    u13 = u13 + [lst[17]]
    u14 = u14 + [lst[18]]
    u15 = u15 + [lst[19]]
    u16 = u16 + [lst[20]]
    u21 = u21 + [lst[21]]
    u22 = u22 + [lst[22]]
    u23 = u23 + [lst[23]]
    u24 = u24 + [lst[24]]
    u25 = u25 + [lst[25]]
    u26 = u26 + [lst[26]]
    u27 = u27 + [lst[27]]
    u28 = u28 + [lst[28]]
    UVMEAN = UVMEAN + [lst[29]]



fig5 = plt.figure()
ax5 = plt.subplot(1,1,1)
ax5.set_ylim([-0.04, 0.04])

    
scale = 5
eventText='Not Distracted' 
ylabel=''   
pps = ppsBlue # note this is retrieved from previous code 
preTrial = 10

ax5.plot(np.asarray(b11).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b12).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b13).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b14).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b15).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b16).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b21).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b22).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b23).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b24).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b25).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b26).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b27).transpose(), c='lightblue', alpha=0.6)
ax5.plot(np.asarray(b28).transpose(), c='lightblue', alpha=0.6)

ax5.plot(np.asarray(u11).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u12).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u13).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u14).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u15).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u16).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u21).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u22).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u23).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u24).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u25).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u26).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u27).transpose(), c='thistle', alpha=0.6)
ax5.plot(np.asarray(u28).transpose(), c='thistle', alpha=0.6)


ax5.plot(np.asarray(BLUEMEAN).transpose(), c='blue', alpha=1)
ax5.plot(np.asarray(UVMEAN).transpose(), c='purple', alpha=1)

ax5.set(ylabel = chr(916) + 'df')
ax5.yaxis.label.set_size(14)
ax5.xaxis.set_visible(False)
        
scalebar = scale * pps

yrange = ax5.get_ylim()[1] - ax5.get_ylim()[0]
scalebary = (yrange / 10) + ax5.get_ylim()[0]
scalebarx = [ax5.get_xlim()[1] - scalebar, ax5.get_xlim()[1]]

ax5.plot(scalebarx, [scalebary, scalebary], c='k', linewidth=2)
ax5.text((scalebarx[0] + (scalebar/2)), scalebary-(yrange/50), str(scale) +' s', ha='center',va='top', **Calibri, **Size)
 
ax5.spines['right'].set_visible(False)
ax5.spines['top'].set_visible(False)
ax5.spines['bottom'].set_visible(False)

xevent = pps * preTrial  
ax5.plot([xevent, xevent],[ax5.get_ylim()[0], ax5.get_ylim()[1] - yrange/20],'--')
ax5.text(xevent, ax5.get_ylim()[1], eventText, ha='center',va='bottom', **Calibri, **Size)


#NEED TO make a mult shaded figure here using each mean as a "trial" then get 
# a shaded figure of the means means with SEM error bars
# Figure out the issue of data types 


#=====================================================================


# Looking at function from Murphy et al (2017)

   
'''
Commented out to test different rats on single trial plot)
    
'''
# Burst analysis for lengths and pauses before and after bursts or runsß
burstanalysis = lickCalc(examplerat['licks'], offset=examplerat['licks_off'])

meanburstlength = np.mean(np.asarray(burstanalysis['bLicks'] ))
meanrunlength = np.mean(burstanalysis['rLicks'])
medburstlen = np.median(np.asarray(burstanalysis['bLicks'] ))
medrunlen = np.median(burstanalysis['rLicks'])
#modburstlen = stats.mode(np.asarray(burstanalysis['bLicks'] ))
#modrunlen = stats.mode(np.asarray(burstanalysis['rLicks'] ))

print('Mean burst length is', meanburstlength, '/ median is', medburstlen, '/mode is') #modburstlen)
print('Mean run length is', meanrunlength, '/ median is', medrunlen, '/mode is') # modrunlen)

figure10 = plt.figure()
plt.hist(burstanalysis['bLicks'])
plt.show()

figure11 = plt.figure()
plt.hist(burstanalysis['rLicks'])
plt.show()



# Maybe some visual representation of licking across a session ?
# Plot the ttls? 
# Just one example for lick day and distraction day 

#for i in blueSnips:
 #   plt.plot(i)


''' Want to plot each trial alone, separate by distracted or not 
    and add the licks TTLs as markers on the plot 
    graphical way to explain distraction trigger/distracted etc.
    and raw data plot example. 
'''

triallicks = nearestevents(examplerat['distractors'], examplerat['licks'])
trialdistractors = nearestevents(examplerat['distractors'], examplerat['distractors'])
trialdistracted = nearestevents(examplerat['distractors'], examplerat['distracted'])
trialnotdistracted = nearestevents(examplerat['distractors'], examplerat['notdistracted'])

trial = 8


f = plt.Figure()
ax = plt.subplot(111)

ax.plot(blueSnips[trial])
ax.plot(uvSnips[trial])

xvals1 = [(x+10)*10 for x in triallicks[trial]]
xvals2 = [(x+10)*10 for x in trialdistractors[trial]]
xvals3 = [(x+10)*10 for x in trialdistracted[trial]]
xvals4 = [(x+10)*10 for x in trialnotdistracted[trial]]


yvals1 = [ax.get_ylim()[1]] * len(xvals1)
yvals2 = [ax.get_ylim()[1] + 0.005] * len(xvals2)
yvals3 = [ax.get_ylim()[1] + 0.01] * len(xvals3) 
yvals4 = [ax.get_ylim()[1] + 0.01] * len(xvals4)


#ax.scatter(xvals, yvals)
ax.scatter(xvals1, yvals1, marker='|')
ax.scatter(xvals2, yvals2, marker='*')
ax.scatter(xvals3, yvals3, marker='o', c='green')
ax.scatter(xvals4, yvals4, marker='x', c='red')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#ax.plot([100,100], [ax.get_ylim()[1], ax.get_ylim()[0]])


# Post distraction pause rater plot 

def distractionrasterFig(ax, timelock, events,
                         pre = 1, post = 1,
                         sortevents=None, sortdirection='ascending'):

    if sortevents != None:
        if len(timelock) != len(sortevents):
            print('Length of sort events does not match timelock events; no sorting')
        else:
            if sortdirection == 'ascending':
                sortOrder = np.argsort(sortevents)
            else:
                sortOrder = np.argsort(sortevents)[::-1]
                
            timelock = [timelock[i] for i in sortOrder]
    
    rasterData = [[] for i in timelock]
    
    for i,x in enumerate(timelock):
        rasterData[i] = [j-x for j in events if (j > x-pre) & (j < x+post)]

#    for ith, trial in enumerate(rasterData):
#        if ith < 26:
# 
#            ax.vlines(trial, ith + .5, ith + 1.5)
#        else:
#            ax.vlines(trial, ith + .5, ith + 1.5, color='blue')
#            
            
    for ith, trial in enumerate(rasterData): 
        xvals = [x for x in trial]
        yvals = [ith+0.5] * len(xvals) 
        ax.scatter(xvals, yvals, marker='|', color='k')
        
        
       
# produces the index in the lick data where the distractor was (indices1)
# now use these indices to add one and subtract the VALUE at index+1 from the VALUE at index
indices1 = []       
for index, value in enumerate(examplerat['distractors']):
    a = np.where(examplerat['licks'] == value) 
    indices1.append(a)       

pdps = []
for tupl in indices1:
    i = tupl[0][0]
    if i+1 < len(examplerat['licks']):
        
        pdp = (examplerat['licks'][i+1] - examplerat['licks'][i])
        pdps.append(pdp)    

# Check the PDPs first one is very long?Yes it it 
#
pdps.append(0)        
figure12 = plt.figure()
ax6 = plt.subplot(111)

rasterPlot = distractionrasterFig(ax6, examplerat['distractors'], examplerat['licks'], pre=1, post=10, sortevents=pdps, sortdirection='ascending')

