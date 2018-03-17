#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# can import this as it is in the same folder as this script 
from AllFunctions import *
import matplotlib.patches as mpatches

'''
Plots for MMiN18 poster  LICK DAY ONLY 

Figure 1a and 1b - Histograms for burst(a) and run(b) lengths last lick day (all rats)
Figure 2 - Photometry analysis (14 rats) individual plots alligned to first lick of BURST and RUN
Figure 3 - Photometry mean of all 14 rats (means of their runs all together)
Figure 4 - Long timecours licking 
Figure 5 - ....
Figure 6 - ...
Figure 7 - 

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
allRunIndices = []
allrILIs = []
allbILIs = []
# Loop through files and calculate burst and run lengths
for filename in TDTfileslist:
    
    file = TDTfilepath + filename
    ratdata = loadmatfile(file)
    burstanalysis = lickCalc(ratdata['licks'], offset=ratdata['licks_off'])
    burstList = burstanalysis['bLicks'] # type, array 
    runList = burstanalysis['rLicks'] # type array
#    indexRunList = burstanalysis['rInd'] 
    runILIs = burstanalysis['rILIs']
    burstILIs = burstanalysis['bILIs']
    
    allBursts.append(burstList)
    allRuns.append(runList)
#    allRunIndices.append(indexRunList)
    allrILIs.append(runILIs)
    allbILIs.append(burstILIs)
    
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

plt.hist(MergedRunList, bins=100, normed=0, facecolor='darkorange') 
plt.xlabel('Licks per run', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xlim(xmax=500, xmin=0)
plt.text(200, 50, 'Mean licks per run '+'{}'.format(meanrunlength), fontsize=14)
plt.text(200, 40, 'Median licks per run '+'{}'.format(medrunlen), fontsize=14)

# get rid of the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.show()

#figure2.savefig('/Volumes/KPMSB352/PHOTOMETRY MMIN18/PDF figures/Hist_Runs.pdf', bbox_inches="tight") 

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
allRatLicks = []
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
    
    allRatLicks.append(ratdata['licks'])

##########################################################################

blueMeansBurst = []
uvMeansBurst = []

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

 # these four lines used later to define means plot (made after runs)
    blueMean = np.mean(blueSnips, axis=0)
    blueMeansBurst.append(blueMean)
    uvMean = np.mean(uvSnips, axis=0)
    uvMeansBurst.append(uvMean)
    
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
    
    # !!! These four lines need to be added to burst code for the mean plot --> 
    
fig5 = plt.figure()
ax3 = plt.subplot(1,1,1)
ax3.set_ylim([-0.04, 0.04])


scale = 5
eventText='First lick in run' 
ylabel=''   
pps = ppsBlue # note this is retrieved from previous code 
preTrial = 10

# Plot all the blue means (means of runs for each rat as 1 line)
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
ax3.yaxis.label.set_size(14)
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


### Repeat for first lick in burst to check if it looks any good (or whether to not bother)
## remember code added to the burst section above (not in a linear way)
## wrote the RUN mean plot code first then the burst mean plot

fig6 = plt.figure()
ax4 = plt.subplot(1,1,1)
ax4.set_ylim([-0.04, 0.04])


scale = 5
eventText='First lick in burst' 
ylabel=''   
pps = ppsBlue # note this is retrieved from previous code 
preTrial = 10

# Plot all the blue means (means of runs for each rat as 1 line)
ax4.plot(np.asarray(blueMeansBurst).transpose(), c='lightblue', alpha=0.6)
ax4.plot(np.asarray(uvMeansBurst).transpose(), c='thistle', alpha=0.6)

# Blue mean of means
# UV mean of means
BLUEMEANSMEANburst = np.mean(blueMeansBurst, axis=0)
UVMEANSMEANburst = np.mean(uvMeansBurst, axis=0)
ax4.plot(np.asarray(BLUEMEANSMEANburst).transpose(), c='blue', alpha=1)
ax4.plot(np.asarray(UVMEANSMEANburst).transpose(), c='purple', alpha=1)

# Plot properties 
ax4.set(ylabel = chr(916) + 'df')
ax4.yaxis.label.set_size(14)
ax4.xaxis.set_visible(False)
scalebar = scale * pps
yrange = ax4.get_ylim()[1] - ax4.get_ylim()[0]
scalebary = (yrange / 10) + ax4.get_ylim()[0]
scalebarx = [ax4.get_xlim()[1] - scalebar, ax4.get_xlim()[1]]
ax4.plot(scalebarx, [scalebary, scalebary], c='k', linewidth=2)
ax4.text((scalebarx[0] + (scalebar/2)), scalebary-(yrange/50), str(scale) +' s', ha='center',va='top', **Calibri, **Size) 
ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)
ax4.spines['bottom'].set_visible(False)
xevent = pps * preTrial  
ax4.plot([xevent, xevent],[ax4.get_ylim()[0], ax4.get_ylim()[1] - yrange/20],'--')
ax4.text(xevent, ax4.get_ylim()[1], eventText, ha='center',va='bottom', **Calibri, **Size)


fig7 = plt.figure()
ax5 = plt.subplot(1,1,1)
ax5.set_ylim([-0.04, 0.04])
runMultFig = trialsMultShadedFig(ax5, [np.asarray(uvMeans),np.asarray(blueMeans)], ppsBlue, eventText='First Lick in Run')
ax5.set(ylabel = chr(916) + 'F')
ax5.yaxis.label.set_size(14)

fig8 = plt.figure()
ax6 = plt.subplot(1,1,1)
ax6.set_ylim([-0.04, 0.04])
burstMultFig = trialsMultShadedFig(ax6, [np.asarray(uvMeansBurst),np.asarray(blueMeansBurst)], ppsBlue, eventText='First Lick in Burst')
ax6.set(ylabel = chr(916) + 'F')
ax6.yaxis.label.set_size(14)
fig7.savefig('/Volumes/KPMSB352/PHOTOMETRY MMIN18/PDF figures/PhotoALL_RUNS.pdf', bbox_inches="tight") 


#==================================

# Figure N?? Probably the first on the poster 

# Long trial figure, 10 min snapshot of one rat licking / photo

fig9 = plt.figure(figsize=(12,2))
ax7 = plt.subplot(1,1,1)
plt.plot(allRatBlue[12], color='royalblue')
plt.plot(allRatUV[10], color='darkorchid')
ax7.set_xticks([0,(10*60*allRatFS[0]),(20*60*allRatFS[0]),(30*60*allRatFS[0]),(40*60*allRatFS[0]),(50*60*allRatFS[0]),(60*60*allRatFS[0])] )
ax7.set_xticklabels([0,10,20,30,40,50,60])
ax7.set_xlabel('Mins', fontsize=14)
#ax7.set_xlim([500000,700000]) # looks really nice scale wise, approx 3 mins
ax7.set_xlim([122070.31494140625,732421.8896484375]) # 2 mins to 12 mins, a 10 min snip without noise at start
ax7.set_ylim([400,800])

# Adding the scatter to long time course plot of photo signals
#allRatLicks.append(ratdata['licks'])
multipliedLicks = []
for element in allRatLicks[12]:
    multElement = element*allRatFS[0]
    multipliedLicks.append([multElement])
    
xvals = multipliedLicks
yvals = [ax7.get_ylim()[1] - 100] * len(xvals)
ax7.scatter(xvals, yvals, marker='|', color='k', linewidth=0.2)

# Get rid of the spines and add labels and ticks to plot 
# Add a 1 minute scale bar OR tick labels for mins 
ax7.set(ylabel = '∆F')
ax7.yaxis.label.set_size(14)
ax7.xaxis.set_visible(False)
            
scalebar = 1*allRatFS[0]*60 # 1 minute

yrange = ax7.get_ylim()[1] - ax7.get_ylim()[0]
scalebary = (yrange / 10) + ax7.get_ylim()[0]
scalebarx = [ax7.get_xlim()[1] - scalebar, ax7.get_xlim()[1]]
ax7.plot(scalebarx, [scalebary, scalebary], c='k', linewidth=2)
ax7.text((scalebarx[0] + (scalebar/2)), scalebary-(yrange/50), '1 Min', ha='center',va='top', **Calibri, **Size)
ax7.spines['right'].set_visible(False)
ax7.spines['top'].set_visible(False)
ax7.spines['bottom'].set_visible(False)
#fig9.savefig('/Volumes/KPMSB352/PHOTOMETRY MMIN18/PDF figures/LongTimeCourse.pdf', bbox_inches="tight") 





# Separating data by quartiles
# Find the quartiles - of the whole data set or each rat? - do both

#(1) ALL RATS AS ONE LIST 

# Produces an index of the upper, lower quartile status of each vurst length
# Use these indices (ie. if == UPPER) to access data 

aggregateLowerQuart = np.percentile(MergedRunList,25)
aggregateUpperQuart = np.percentile(MergedRunList,75) 
    
allLogIndRuns = []
for runLicksList in allRuns:
    logIndRuns = [] # so 14 empty arrays exist and then don't (add to larger)
    for item in runLicksList:
        if item < aggregateLowerQuart:
            logIndRuns.append('UPPER')
        else:
            if item > aggregateUpperQuart:
                logIndRuns.append('LOWER')
            
            else:
                logIndRuns.append('MIDDLE')
    allLogIndRuns.append(logIndRuns)
            
# 14 lists of logical indices for whether the n licks in that run was L,M,U

 
#### =========================================== 

# Figure 10 - Finding the pauses before run (preRunPauses) and how this relates
# to burst length 
# regression? As both continuous??? 

# Linear regression --> see R notes 


    
#rILIs are these the ILIs for before the first lick or not??? 

# MergedRunList exists already
MergedrILIsList = list(itertools.chain.from_iterable(allrILIs)) 
fig10 = plt.figure()
ax8 = plt.subplot(1,1,1)
ax8.scatter(MergedrILIsList, MergedRunList, marker='*', color='k') #linewidth=0.2)   
#ax8.set_xlim([0,400]) 
#ax8.set_ylim([0,400])
    
# Run linear regression, can preRunPause predict the runLength?
# Can repeat this for bursts too (higher sample size may be more informative)
# Poor looking fit, possibly correlated at the extremes (very long/short)
import scipy.stats as scipys
slope, intercept, r_value, p_value, std_err = scipys.linregress(MergedrILIsList, MergedRunList)
print("r-squared:", r_value**2)

#+++++++++++++++++++++++++ repeated for bursts, ILIs versus burst lengths ++++++++++++++

MergedbILIsList = list(itertools.chain.from_iterable(allbILIs))
# MergedBurstList already exists 
fig11 = plt.figure()
ax9 = plt.subplot(1,1,1)
ax9.scatter(MergedbILIsList, MergedBurstList, color='k') #linewidth=0.2) 
    # A lot of them are very short and very small pauses before bursts, 
    # probably not linear fit but do linreg anyway    
slopeB, interceptB, r_valueB, p_valueB, std_errB = scipys.linregress(MergedbILIsList, MergedBurstList)
print("r-squaredb:", r_valueB**2)


# Could t-test difference the pre-burst pauses for SHORT (quart) and for LONG

# Figure out how to separate these pauses based on long and short (if, index == long)




# *******************************************************************

# Figure 12? Photometry plots (averaged) aligned to short and long runs, is there a difference?
# Firstly separate out the run lists (and then the times) into short and long 


# Final lists of run times sorted by u.m.l and stored by rat (14 lists)
lowerqRunTimes = []
uppqRunTimes = []
mid50RunTimes = []

# Might need the index and the value for both lists ??
for i, listofindices in enumerate(allLogIndRuns):
    templower = []
    tempupper = []
    tempmid = []
    for j, runIndex in enumerate(listofindices):
        
        #print(i,j) i is the list index and j is the item index
        
        if runIndex == 'LOWER':
            lowrun = allRunsTimes[i][j]
            templower.append(lowrun)
               
        if runIndex == 'UPPER':
            upprun = allRunsTimes[i][j]
            tempupper.append(upprun)
#                
        if runIndex == 'MIDDLE':
            midrun = allRunsTimes[i][j]
            tempmid.append(midrun)
            
    lowerqRunTimes.append(templower)
    uppqRunTimes.append(tempupper)
    mid50RunTimes.append(tempmid)
    
# _________________________________________________________________________

    
''' 
         
allign to lowerqRunTimes
allign to uppqRunTimes

# Then, if not too complex, add BOTH BLUE SIGNALS high and low burst numbers to the 
    # same photometry plot 

'''

uvMeans_short_run = []
blueMeans_short_run = []
uvMeans_long_run = []
blueMeans_long_run = []
# Makes tonnes of individual plots             
# Individual rats might look odd as low Ns, but mean of mean will be better 
# Repeat this with bursts if looks like might be useful 

for i, val in enumerate(lowerqRunTimes):
    try:
        # make a blue and uv snip for all 14, and noise remover / index
        blueSnips, ppsBlue = snipper(allRatBlue[i], lowerqRunTimes[i], fs=allRatFS[i], bins=300)
        uvSnips, ppsUV = snipper(allRatUV[i], lowerqRunTimes[i], fs=allRatFS[i], bins=300)
    
        randevents = makerandomevents(allRatBlue[i][300], allRatBlue[i][-300])
        bgMad, bgMean = findnoise(allRatBlue[i], randevents, fs=allRatFS[i], method='sum', bins=300)
        threshold = 1
        sigSum = [np.sum(abs(i)) for i in blueSnips]
        noiseindex = [i > bgMean + bgMad*threshold for i in sigSum]
        # Might not need the noise index, this is just for trials fig 
    except: 
        pass
    
    fig12 = plt.figure()
    ax10 = plt.subplot(1,1,1)
    ax10.set_ylim([-0.03, 0.03])
    #ax.set_ylim([-0.05, 0.05])
    trialsMultShadedFig(ax10, [uvSnips,blueSnips], ppsBlue, eventText='First Lick Short Run')
    plt.text(250,0.03, '{}'.format(len(lowerqRunTimes[i])) + ' short runs' )
    
    fig13 = plt.figure()
    ax11 = plt.subplot(1,1,1)
    ax11.set_ylim([-0.2, 0.2])
    trialsFig(ax11, blueSnips, uvSnips, ppsBlue, eventText='First Lick in Short Run', noiseindex=noiseindex) #, )
    plt.text(250,0.2, '{}'.format(len(lowerqRunTimes[i])) + ' short runs' )

# # these four lines used later to define means plot (made after runs)
    blueMeanSHORT = np.mean(blueSnips, axis=0)
    blueMeans_short_run.append(blueMeanSHORT)
    uvMeanSHORT = np.mean(uvSnips, axis=0)
    uvMeans_short_run.append(uvMeanSHORT)


## ===============================================================

# Photometry figures (individual) for LONG bursts 

for i, val in enumerate(uppqRunTimes):
    try:
        # make a blue and uv snip for all 14, and noise remover / index
        blueSnips, ppsBlue = snipper(allRatBlue[i], uppqRunTimes[i], fs=allRatFS[i], bins=300)
        uvSnips, ppsUV = snipper(allRatUV[i], uppqRunTimes[i], fs=allRatFS[i], bins=300)
    
        randevents = makerandomevents(allRatBlue[i][300], allRatBlue[i][-300])
        bgMad, bgMean = findnoise(allRatBlue[i], randevents, fs=allRatFS[i], method='sum', bins=300)
        threshold = 1
        sigSum = [np.sum(abs(i)) for i in blueSnips]
        noiseindex = [i > bgMean + bgMad*threshold for i in sigSum]
        # Might not need the noise index, this is just for trials fig 
    except: 
        pass
    
    fig14 = plt.figure()
    ax12 = plt.subplot(1,1,1)
    ax12.set_ylim([-0.03, 0.03])
    #ax.set_ylim([-0.05, 0.05])
    trialsMultShadedFig(ax12, [uvSnips,blueSnips], ppsBlue, eventText='First Lick Long Run')
    plt.text(250,0.03, '{}'.format(len(uppqRunTimes[i])) + ' long runs' )
    
    fig14 = plt.figure()
    ax13 = plt.subplot(1,1,1)
    ax13.set_ylim([-0.2, 0.2])
    trialsFig(ax13, blueSnips, uvSnips, ppsBlue, eventText='First Lick in Long Run', noiseindex=noiseindex) #, )
    plt.text(250,0.2, '{}'.format(len(uppqRunTimes[i])) + ' long runs' )

# # these four lines used later to define means plot (made after runs) 
    blueMeanLONG = np.mean(blueSnips, axis=0)
    blueMeans_long_run.append(blueMeanLONG)
    uvMeanLONG = np.mean(uvSnips, axis=0)
    uvMeans_long_run.append(uvMeanLONG)
    
### Means figures for short and long bursts 

# JUST the error bard type figure (mult shaded) make with blue and uv then make 
# with blue from short and blue from long 

fig15 = plt.figure(figsize=(6,3))
ax14 = plt.subplot(1,1,1)
ax14.set_ylim([-0.05, 0.05])
SHORTrunMultFig = trialsMultShadedFig(ax14, [np.asarray(uvMeans_short_run),np.asarray(blueMeans_short_run)], ppsBlue, eventText='', scale=0) #First Lick in Short Run
ax14.set(ylabel = chr(916) + 'F')
ax14.yaxis.label.set_size(14)
#fig15.savefig('/Volumes/KPMSB352/PHOTOMETRY MMIN18/PDF figures/PhotoMultSHORTRUN.pdf', bbox_inches="tight") 

fig16 = plt.figure(figsize=(6,3))
ax15 = plt.subplot(1,1,1)
ax15.set_ylim([-0.05, 0.05])
LONGrunMultFig = trialsMultShadedFig(ax15, [np.asarray(uvMeans_long_run),np.asarray(blueMeans_long_run)], ppsBlue, eventText='') #First Lick in Long Run
ax15.set(ylabel = chr(916) + 'F')
ax15.yaxis.label.set_size(14)
#fig16.savefig('/Volumes/KPMSB352/PHOTOMETRY MMIN18/PDF figures/PhotoMultLONGRUN.pdf', bbox_inches="tight") 

## Both short and long runs on the same graph (just blue signals)

fig17 = plt.figure(figsize=(6,3))
ax16 = plt.subplot(1,1,1)
ax16.set_ylim([-0.05, 0.05])
LONG_SHORTrunMultFig = trialsMultShadedFig(ax16, [np.asarray(blueMeans_short_run),np.asarray(blueMeans_long_run)], ppsBlue, eventText=''
                                                  , linecolor=['k', 'firebrick'], errorcolor=['darkgrey', 'darkorange'], scale=0)
ax16.set(ylabel = chr(916) + 'F')
ax16.yaxis.label.set_size(14)

# Simple figure legend
orange_patch = mpatches.Patch(color='darkorange', label='Long Runs')
grey_patch = mpatches.Patch(color='darkgrey', label='Short Runs')
plt.legend(handles=[orange_patch, grey_patch], fontsize=14)
plt.show()

#fig17.savefig('/Volumes/KPMSB352/PHOTOMETRY MMIN18/PDF figures/PhotoMultORANGE.pdf', bbox_inches="tight") 


