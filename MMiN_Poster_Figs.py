#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Plots for MMiN18 poster 
Figure 1 and 2 - Histograms for burst and run lengths last lick day (all rats)
Figure 3
Figure 4
Figure 5
Figure 6
Figure 7

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
    
# Burst histogram, frequency of different burst lengths all rats, last lick day
figure1 = plt.figure()
plt.hist(MergedBurstList, bins=100, normed=1, facecolor='blue', alpha=0.5)
plt.title('Insert plot title')
plt.xlabel('Licks per burst')
plt.ylabel('Probability')
plt.xlim(xmax=50, xmin=0)
plt.show()

# Run histogram, frequency of different run lengths across all rats
figure2 = plt.figure()
plt.hist(MergedRunList, bins=100, normed=1, facecolor='green', alpha=0.5) #Maybe add normed=True
plt.title('Insert plot title')
plt.xlabel('Licks per run')
plt.ylabel('Probability')
plt.xlim(xmax=500, xmin=0)
plt.show()

# Add mean and median text to plots 



# Descriptives - aggregated data

meanburstlength = np.mean(MergedBurstList)
medburstlen = np.median(MergedBurstList)
meanrunlength = np.mean(MergedRunList)
medrunlen = np.median(MergedRunList)

## Descriptives, means and medians from each rat then then mean of those
#
#for each list in the all burst list:
#    find the mean 
#    add to list
#    find the median
#    add to list
#    
#    find mean of mean list
#    find mean of median list
#    

    
    