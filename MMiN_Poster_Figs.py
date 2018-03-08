#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Plots for MMiN18 poster 
Figure 1a and 1b - Histograms for burst(a) and run(b) lengths last lick day (all rats)
Figure 2 - Photometry analysis (14 rats) individual plots alligned to first lick of BURST and RUN
Figure 3
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


# Burst histogram, frequency of different burst lengths all rats, last lick day


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


# Run histogram, frequency of different run lengths across all rats
figure2 = plt.figure()

plt.hist(MergedRunList, bins=100, normed=1, facecolor='gold') #Maybe add normed=True
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

bMeanByRat = []
bMedianByRat = []
for bList in allBursts:
    meanB = np.mean(bList)
    bMeanByRat.append(meanB)
    medB = np.median(bList)
    bMedianByRat.append(medB)

meanMeanBurst = np.mean(bMeanByRat) # Similar (rounds to the same) for aggregate
meanMedBurst = np.mean(bMedianByRat) # Similar as aggregate
    
rMeanByRat = []
rMedianByRat = []
for rList in allRuns:
    meanR = np.mean(rList)
    rMeanByRat.append(meanR)
    medR = np.median(rList)
    rMedianByRat.append(medR)

meanMeanRun = np.mean(rMeanByRat) # Agg = 143, Individual = 155.60
meanMedRun = np.mean(rMedianByRat) # Agg = 80, Individual = 115.78
    
   
    