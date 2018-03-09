#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# can import this as it is in the same folder as this script 
from AllFunctions import *
'''
Plots for MMiN18 poster 
Figure 1a and 1b - Histograms for burst(a) and run(b) lengths last lick day (all rats)
Figure 2 - Photometry analysis (14 rats) individual plots alligned to first lick of BURST and RUN
Figure 3 - Photometry mean of all 14 rats (means of their runs all together)
Figure 4
Figure 5
Figure 6

'''

# Figure 1 -----------------------------------------------------------

# TDT file paths for the last lick day for THPH1 and THPH2 rats (n=12)
TDTfileslist = ['thph1.1lick6', 'thph1.2lick6','thph1.3lick6','thph1.4lick6',
                'thph1.5lick6','thph1.6lick6','thph2.1lick3','thph2.2lick3',
                'thph2.3lick3', 'thph2.4lick3','thph2.5lick3','thph2.6lick3',
                'thph2.7lick6', 'thph2.8lick6']

TDTfilepath = '/Volumes/KPMSB352/PHOTOMETRY MMIN18/'


# Assign empty lists for storing arrays of burst/run lengths
allBursts = []
allRuns = []
# Loop through files and calculate burst and run lengths
for filename in TDTfileslist:
    
    file = TDTfilepath + filename
    ratdata = loadmatfile(file)
    burstanalysis = lickCalc(ratdata['licks'], offset=ratdata['licks_off'])
    burstList = burstanalysis['bLicks'] # type, array 
    runList = burstanalysis['rLicks'] # type array
    allBursts.append(burstList)
    allRuns.append(runList)
    
# Make the list of lists into one long list for histogram 
MergedBurstList = list(itertools.chain.from_iterable(allBursts)) 
MergedRunList = list(itertools.chain.from_iterable(allRuns)) 
    
# Descriptives - aggregated data
meanburstlength = round(np.mean(MergedBurstList))
medburstlen = round(np.median(MergedBurstList))
meanrunlength = round(np.mean(MergedRunList))
medrunlen = round(np.median(MergedRunList))


# 1a - Burst histogram, frequency of burst lengths all rats, last lick day
figure1 = plt.figure()
plt.hist(MergedBurstList, bins=100, normed=1, facecolor='cornflowerblue')
plt.xlabel('Licks per burst', fontsize=14)
plt.ylabel('Probability', fontsize=14)
plt.xlim(xmax=50, xmin=0)
plt.text(20, 0.10, 'Mean licks per burst '+'{}'.format(meanburstlength), fontsize=14)
plt.text(20, 0.09, 'Median licks per burst '+'{}'.format(medburstlen), fontsize=14)
# get rid of the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.show()


# 1b - Run histogram, frequency of run lengths all rats, last lick day
figure2 = plt.figure()

plt.hist(MergedRunList, bins=100, normed=1, facecolor='gold') 
plt.xlabel('Licks per run', fontsize=14)
plt.ylabel('Probability', fontsize=14)
plt.xlim(xmax=500, xmin=0)
plt.text(200, 0.010, 'Mean licks per run '+'{}'.format(meanrunlength), fontsize=14)
plt.text(200, 0.009, 'Median licks per run '+'{}'.format(medrunlen), fontsize=14)

# get rid of the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.show()

#------------------------------------------------------------------------
## Descriptives, means and medians from each rat then then mean of those
# Similar for bursts but quite different for runs aggregated vs indivdual
#
#bMeanByRat = []
#bMedianByRat = []
#for bList in allBursts:
#    meanB = np.mean(bList)
#    bMeanByRat.append(meanB)
#    medB = np.median(bList)
#    bMedianByRat.append(medB)
#
#meanMeanBurst = np.mean(bMeanByRat) # Similar (rounds to the same) for aggregate
#meanMedBurst = np.mean(bMedianByRat) # Similar as aggregate
#    
#rMeanByRat = []
#rMedianByRat = []
#for rList in allRuns:
#    meanR = np.mean(rList)
#    rMeanByRat.append(meanR)
#    medR = np.median(rList)
#    rMedianByRat.append(medR)
#
#meanMeanRun = np.mean(rMeanByRat) # Agg = 143, Individual = 155.60
#meanMedRun = np.mean(rMedianByRat) # Agg = 80, Individual = 115.78
    
 # Figure 2 -----------------------------------------------------------  
'''

'''

# TDT file paths for the last lick day for THPH1 and THPH2 rats (n=12)


# Assign empty lists for storing arrays of burst/run lengths
allBurstsTimes = []
allRunsTimes = []
allRatBlue = []
allRatUV = []
allRatFS = []
# Loop through files and calculate burst and run lengths
for filename in TDTfileslist:
    
    file = TDTfilepath + filename
    ratdata = loadmatfile(file)
    burstanalysis = lickCalc(ratdata['licks'], offset=ratdata['licks_off'])
    burstListTimes = burstanalysis['bStart'] # type, array 
    runListTimes = burstanalysis['rStart'] # type array
    allBurstsTimes.append(burstListTimes)
    allRunsTimes.append(runListTimes)
    
    allRatBlue.append(ratdata['blue'])
    allRatUV.append(ratdata['uv'])
    allRatFS.append(ratdata['fs'])
    

##########################################################################
'''


'''

for i, val in enumerate(allBurstsTimes):
    
    # make a blue and uv snip for all 14, and noise remover / index
    blueSnips, ppsBlue = snipper(allRatBlue[i], allBurstsTimes[i], fs=allRatFS[i], bins=300)
    uvSnips, ppsUV = snipper(allRatUV[i], allBurstsTimes[i], fs=allRatFS[i], bins=300)

    randevents = makerandomevents(allRatBlue[i][300], allRatBlue[i][-300])
    bgMad, bgMean = findnoise(allRatBlue[i], randevents, fs=allRatFS[i], method='sum', bins=300)
    threshold = 1
    sigSum = [np.sum(abs(i)) for i in blueSnips]
    noiseindex = [i > bgMean + bgMad*threshold for i in sigSum]
    # Might not need the noise index, this is just for trials fig 
    
    fig = plt.figure()
    ax = plt.subplot(1,1,1)
    ax.set_ylim([-0.03, 0.03])
    #ax.set_ylim([-0.05, 0.05])
    trialsMultShadedFig(ax, [uvSnips,blueSnips], ppsBlue, eventText='First Lick in Burst')
    plt.text(250,0.03, '{}'.format(len(allBurstsTimes[i])) + ' bursts' )
    
    fig2 = plt.figure()
    ax2 = plt.subplot(1,1,1)
    ax2.set_ylim([-0.2, 0.2])
    trialsFig(ax2, blueSnips, uvSnips, ppsBlue, eventText='First Lick in Burst', noiseindex=noiseindex) #, )
    plt.text(250,0.2, '{}'.format(len(allBurstsTimes[i])) + ' bursts' )

#### Allign to runs - makes individual plots and then plots the average 

blueMeans = []
uvMeans = []

for i, val in enumerate(allRunsTimes):
    
    # make a blue and uv snip for all 14, and noise remover / index
    blueSnips, ppsBlue = snipper(allRatBlue[i], allRunsTimes[i], fs=allRatFS[i], bins=300)
    uvSnips, ppsUV = snipper(allRatUV[i], allRunsTimes[i], fs=allRatFS[i], bins=300)

    randevents = makerandomevents(allRatBlue[i][300], allRatBlue[i][-300])
    bgMad, bgMean = findnoise(allRatBlue[i], randevents, fs=allRatFS[i], method='sum', bins=300)
    threshold = 1
    sigSum = [np.sum(abs(i)) for i in blueSnips]
    noiseindex = [i > bgMean + bgMad*threshold for i in sigSum]
    
    # Might not need the noise index, this is just for trials fig 
    
    fig3 = plt.figure()
    ax = plt.subplot(1,1,1)
    ax.set_ylim([-0.03, 0.03])
    #ax.set_ylim([-0.05, 0.05])
    trialsMultShadedFig(ax, [uvSnips,blueSnips], ppsBlue, eventText='First Lick in Run')
    plt.text(250,0.03, '{}'.format(len(allRunsTimes[i])) + ' runs' )
    
    fig4 = plt.figure()
    ax2 = plt.subplot(1,1,1)
    ax2.set_ylim([-0.2, 0.2])
    trialsFig(ax2, blueSnips, uvSnips, ppsBlue, eventText='First Lick in Run', noiseindex=noiseindex) #, )
    plt.text(250,0.2, '{}'.format(len(allRunsTimes[i])) + ' runs' )

    blueMean = np.mean(blueSnips, axis=0)
    blueMeans.append(blueMean)
    uvMean = np.mean(uvSnips, axis=0)
    uvMeans.append(uvMean)
    
fig5 = plt.figure()
ax3 = plt.subplot(1,1,1)
ax3.set_ylim([-0.04, 0.04])


scale = 5
eventText='First lick in run' 
ylabel=''   
pps = ppsBlue # note this is retrieved from previous code 
preTrial = 10


ax3.plot(np.asarray(blueMeans).transpose(), c='lightblue', alpha=0.6)
ax3.plot(np.asarray(uvMeans).transpose(), c='thistle', alpha=0.6)

# Blue mean of means
# UV mean of means
BLUEMEANSMEAN = np.mean(blueMeans, axis=0)
UVMEANSMEAN = np.mean(uvMeans, axis=0)
ax3.plot(np.asarray(BLUEMEANSMEAN).transpose(), c='blue', alpha=1)
ax3.plot(np.asarray(UVMEANSMEAN).transpose(), c='purple', alpha=1)

# Plot properties 
ax3.set(ylabel = chr(916) + 'df')
ax3.xaxis.set_visible(False)
scalebar = scale * pps
yrange = ax3.get_ylim()[1] - ax3.get_ylim()[0]
scalebary = (yrange / 10) + ax3.get_ylim()[0]
scalebarx = [ax3.get_xlim()[1] - scalebar, ax3.get_xlim()[1]]
ax3.plot(scalebarx, [scalebary, scalebary], c='k', linewidth=2)
ax3.text((scalebarx[0] + (scalebar/2)), scalebary-(yrange/50), str(scale) +' s', ha='center',va='top', **Calibri, **Size) 
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
xevent = pps * preTrial  
ax3.plot([xevent, xevent],[ax3.get_ylim()[0], ax3.get_ylim()[1] - yrange/20],'--')
ax3.text(xevent, ax3.get_ylim()[1], eventText, ha='center',va='bottom', **Calibri, **Size)




  