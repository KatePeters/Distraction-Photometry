#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:31:33 2017

@author: u1490431
"""

#THPH1 Behavioural analysis 


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import statistics as stat
from scipy import stats
import pandas as pd
import os
import sys

sb.set_context("paper")
sb.set_style("white")


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

    
    

    
    

metafile = 'R:\DA_and_Reward\kp259\THPH1AND2\THPH1&2Metafile.csv'
# filename = '/Volumes/KPMSB352/R drive copy 29thJuly/DPCP1/!2017-04-23_11h54m.Subject dpcp1.15' 



metaData  = MetaExtractor(metafile)   
os.chdir('R:\DA_and_Reward\kp259\THPH1AND2\med') 

NDistractors = 0 
distracted = 0
notdistracted = 0
pyDis = []
theoreticalDisAll = [] 
adjustedDistractors = []
#allMedDis = []
allLickDataArray = []
pdps = []

pdpAll = []



for medFileName in metaData['MedFilenames']:    # 32 includes last lick day, 48 does not only distraction
    print(medFileName)
    lickdata = medfilereader(medFileName, 'b', remove_var_header= True)
#    meddistractors = medfilereader(medFileName, 'i', remove_var_header= True)
#    allMedDis.append(meddistractors)
    allLickDataArray.append(lickdata)
    lickdataNum = np.asarray(lickdata)
    pyDis = []
    adjustedDistractors.append(distractionCalc2(lickdata))
    
for ind, lists in enumerate(adjustedDistractors):
    pdp = []
    for value in lists:
        if value in allLickDataArray[ind] and value != allLickDataArray[ind][-1]: #if the value is in this list of licks (from all)
            index = allLickDataArray[ind].index(value)
            pdp.append(allLickDataArray[ind][index+1] - allLickDataArray[ind][index])
    pdpAll.append(pdp)
        #pdpAll.append(pdps) # gives just the last list of pdps or 1st? - len = 4097
                         #something wrong, not going into lists just all appended
                         # why 4089 vs 4097?? If indent once more, what happens here?
meanlist = []
medianlist = []
for day in pdpAll:
    mean = np.mean(day)
    meanlist.append(mean)
    median = np.median(day)
    medianlist.append(median)
    
  
distractedOrNot = []   
distracted2 = []
nondis = []
for pdpList in pdpAll:
    distracted = 0
    nonDis = 0
    for pdp in pdpList:
        if pdp >= 1:
            distracted += 1
        else:
            nonDis += 1
    distractedOrNot.append([distracted, nonDis])
    distracted2.append(distracted)
    nondis.append(nonDis)     
    
meanpdps = []
medianpdps = []

for pdpList in pdpAll:
    mean = np.mean(pdpList)
    median = np.median(pdpList)
    meanpdps.append(mean)
    medianpdps.append(median)




def burstcalc (filename):
    
    data = medfilereader(filename, 'b', remove_var_header= True)
    ILIs = np.diff(data)
    
    # Decide what separates a burst (ie. 0.50 or 0.25)
    ''' Calculate bursts and 3 lick bursts edited from burstlength analysis'''

    # What is this bit of code doing?
    longILIs = [i for i,x in enumerate(ILIs) if x > 0.25]
    bursts = np.diff(longILIs + [len(ILIs)])
    threeLickBursts = len([x for x in bursts if x == 3])
    fourLickBursts = len([x for x in bursts if x == 4])
    fiveLickBursts = len([x for x in bursts if x == 5])
    threeLickBurstsPercent = threeLickBursts/len(bursts)*100
    fourLickBurstsPercent = fourLickBursts/len(bursts)*100
    fiveLickBurstsPercent = fiveLickBursts/len(bursts)*100
    meanBursts = np.mean(bursts)
    medianBursts = stat.median(bursts)

    # Calculate NON- 3 licks and check that all add to 100%
    non3LickBurst = len([x for x in bursts if x != 3])
    non3LickBurstPercent = non3LickBurst/len(bursts)*100
    sanityCheckPercentages = threeLickBurstsPercent + non3LickBurstPercent 
    
    otherburstlength = len([x for x in bursts if x != 3 and x!=4 and x!=5])
    otherpercent = otherburstlength/len(bursts)*100
    
    burstslist = (threeLickBurstsPercent, fourLickBurstsPercent, fiveLickBurstsPercent, otherpercent)
    return {'3Lick%':threeLickBurstsPercent, '4Lick%':fourLickBurstsPercent, '5Lick%':fiveLickBurstsPercent, \
            'OtherPercent':otherpercent}
 

burstlist = [] 
threelick = []
fourlick = []
fivelick = []
otherlick = []

for medFileName in metaData['MedFilenames']:  #56: is all from distraction day 
    burstlist = burstcalc(medFileName)
    threelick.append(burstlist['3Lick%'])
    fourlick.append(burstlist['4Lick%'])
    fivelick.append(burstlist['5Lick%'])
    otherlick.append(burstlist['OtherPercent'])

  
# Code to make excel file of PDP means and medians for later SPSS or R analysis
# Added information on 3,4 and 5 lick percentages in 

d = {'MeanPDPs': meanpdps, 'MedianPDPs': medianpdps, 'Rat': metaData['RatID'], \
     'Session': metaData['Session'], 'Dis':metaData['Distractions'], \
     'Distracted': distracted2, 'NotDis':nondis, '3Lick%':threelick, '4Lick%':fourlick, '5Lick%':fivelick, \
     'Other%' : otherlick}

pandaPDPs = pd.DataFrame(data=d)
headers = ['Mean', 'Median']
pandaPDPs.to_excel('D:\Third year report\THPH1_PDPS.xlsx', index=False) #specify where you want these to go



def cumulativelickFig(ax, firstlick, normed=True, color='g', log=True):
    sorted_data = np.sort(firstlick)
    yvals = np.arange(len(sorted_data)+1)
    
    if normed == True:
        nlicks = len(sorted_data)
        yvals =yvals/nlicks
        
    a = ax.step(np.concatenate([sorted_data, sorted_data[[-1]]]),
             yvals, color=color)
    
    if log == True:
        ax.set_xscale('log', basex=10) # option in funcion as True or False (log setting)
        ax.set_xlim([0.1, 1000])
    return ax, a





# Subset the alllickdataarray, extract important days 

lastlickdaylicks = [allLickDataArray[30], allLickDataArray[31], allLickDataArray[32], allLickDataArray[33], allLickDataArray[35], \
                    allLickDataArray[64], allLickDataArray[65], allLickDataArray[66], allLickDataArray[67], allLickDataArray[68], \
                    allLickDataArray[69], allLickDataArray[88], allLickDataArray[89]]
distractiondaylicks = [allLickDataArray[36], allLickDataArray[37], allLickDataArray[38], allLickDataArray[39], allLickDataArray[41], \
                       allLickDataArray[72], allLickDataArray[73], allLickDataArray[74], allLickDataArray[75], allLickDataArray[76], \
                       allLickDataArray[77], allLickDataArray[90], allLickDataArray[91]]

#Subset pdpAll, extract important days 
lastlickdayPDPs = [pdpAll[30], pdpAll[31], pdpAll[32], pdpAll[33], pdpAll[35], pdpAll[64], pdpAll[65], pdpAll[66], \
                   pdpAll[67], pdpAll[68], pdpAll[69], pdpAll[88], pdpAll[89]]
distractiondayPDPs = [pdpAll[36], pdpAll[37], pdpAll[38], pdpAll[39], pdpAll[41], pdpAll[72], pdpAll[73], pdpAll[74], \
                      pdpAll[75], pdpAll[76], pdpAll[77], pdpAll[90], pdpAll[91]]



# Plot settings, font / size / styles
Calibri = {'fontname':'Calibri'}
Size = {'fontsize': 22}
label_size = 18
plt.rcParams['xtick.labelsize'] = label_size 
plt.rcParams['ytick.labelsize'] = label_size 

plt.rcParams['lines.linewidth'] = 2



# Make cumulative lick plot with average, licks over time (normalised?)
fig = plt.figure()

plt.title('Cumulative licks - lick training', **Calibri, **Size)
ax = fig.add_subplot(111)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)


fig2 = plt.figure()
plt.title('ADD TITLE', **Calibri, **Size)
ax2 = fig2.add_subplot(111)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

fig3 = plt.figure()
plt.title('ADD TITLE', **Calibri, **Size)
ax3 = fig3.add_subplot(111)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)

fig4 = plt.figure()
plt.title('ADD TITLE', **Calibri, **Size)
ax4 = fig4.add_subplot(111)
ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)

fig5 = plt.figure()
plt.title('ADD TITLE', **Calibri, **Size)
ax5 = fig5.add_subplot(111)
ax5.spines['right'].set_visible(False)
ax5.spines['top'].set_visible(False)

fig6 = plt.figure()
plt.title('ADD TITLE', **Calibri, **Size)
ax6 = fig6.add_subplot(111)
ax6.spines['right'].set_visible(False)
ax6.spines['top'].set_visible(False)

fig7 = plt.figure()
plt.title('ADD TITLE', **Calibri, **Size)
ax7 = fig7.add_subplot(111)
ax7.spines['right'].set_visible(False)
ax7.spines['top'].set_visible(False)

fig8 = plt.figure()
plt.title('ADD TITLE', **Calibri, **Size)
ax8 = fig8.add_subplot(111)
ax8.spines['right'].set_visible(False)
ax8.spines['top'].set_visible(False)

# CUMULATIVE LICKS
# Plots all for lick day with average
# Adding mean line into plot, by adding ALL values in normed mode, wll effectively give average
for index, licklist in enumerate(lastlickdaylicks):
    plot = cumulativelickFig(ax, lastlickdaylicks[index], normed=True, color='lightgrey', log=False)

# Adding mean line into plot, by adding ALL values in normed mode, wll effectively give average
avg = [item for rat in lastlickdaylicks for item in rat] 
cumulativelickFig(ax, avg, normed=True, color='darkorange', log=False)

# Plots all for distraction day with average 
for index, licklist in enumerate(distractiondaylicks):
    plot = cumulativelickFig(ax2, distractiondaylicks[index], normed=True, color='lightgrey', log=False)

avg2 = [item for rat in distractiondaylicks for item in rat] 
cumulativelickFig(ax2, avg2, normed=True, color='deepskyblue', log=False)






# Averages for lickplot, orange is lick training, blue is distraction 
cumulativelickFig(ax4, avg, normed=True, color='darkorange', log=False)
cumulativelickFig(ax4, avg2, normed=True, color='deepskyblue', log=False)
#cumulativelickFig(ax4, avg3, normed=True, color='grey', log=False)



# CUMULATIVE PDPS
# Plots all for lick day with average

for index, licklist in enumerate(lastlickdayPDPs):
    plot = cumulativelickFig(ax5, lastlickdayPDPs[index], normed=True, color='lightgrey', log=True)

# Adding mean line into plot, by adding ALL values in normed mode, wll effectively give average
avg4 = [item for rat in lastlickdayPDPs for item in rat] 
cumulativelickFig(ax5, avg4, normed=True, color='seagreen', log=True)

# Plots all for distraction day with average 
for index, licklist in enumerate(distractiondayPDPs):
    plot = cumulativelickFig(ax6, distractiondayPDPs[index], normed=True, color='lightgrey', log=True)

avg5 = [item for rat in distractiondayPDPs for item in rat] 
cumulativelickFig(ax6, avg5, normed=True, color='gold', log=True)

##Amphetamine 
#for index, licklist in enumerate(amphetaminePDPs):
#    plot = cumulativelickFig(ax7, amphetaminePDPs[index], normed=True, color='lightgrey', log=False)

#avg6 = [item for rat in amphetaminePDPs for item in rat] 
#cumulativelickFig(ax7, avg6, normed=True, color='k', log=False)


# Averages for lickplot, orange is lick training, blue is distraction 
cumulativelickFig(ax8, avg4, normed=True, color='seagreen', log=True)
cumulativelickFig(ax8, avg5, normed=True, color='gold', log=True)
#cumulativelickFig(ax8, avg6, normed=True, color='k', log=True)










