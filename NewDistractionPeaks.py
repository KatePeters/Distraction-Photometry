#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 17:14:10 2018

@author: u1490431
"""

# Distracted or not peaks

TDTfileslist = ['thph1.1distraction2', 'thph1.2distraction2','thph1.3distraction2',
                'thph1.4distraction2', 'thph1.5distraction2','thph1.6distraction2',
                'thph2.1distraction','thph2.2distraction','thph2.3distraction', 
                'thph2.4distraction','thph2.5distraction','thph2.6distraction',
                'thph2.7distraction', 'thph2.8distraction']

TDTfilepath = '/Volumes/KPMSB352/PHOTOMETRY MMIN18/'


# Assign empty lists for storing arrays of burst/run lengths
allDistracted = []
allNotDistracted = []
allDistractors = []
allRatLicks = []
allRatBlue = []
allRatUV = []
allRatFS = []
# Loop through files and extracts all info needed for snips 
for filename in TDTfileslist:
    
    file = TDTfilepath + filename
    ratdata = loadmatfile(file)
    distracted = ratdata['distracted']
    notdistracted = ratdata['notdistracted']
    distractors = ratdata['distractors']
        
    allRatBlue.append(ratdata['blue'])
    allRatUV.append(ratdata['uv'])
    allRatFS.append(ratdata['fs'])
    
    allRatLicks.append(ratdata['licks'])
    allDistracted.append(distracted)
    allNotDistracted.append(notdistracted)
    allDistractors.append(distractors)

# ===============================================================================
# ===============================================================================
# ===============================================================================
# ===============================================================================

# Calculating different peaks, and means based on on DISTRACTED and NOT DISTRACTED
# To find peaks and averaged activity across time 

# Called means because give 14 arrays which are the MEAN for each rat 
allblueMeans = []
alluvMeans = []
for i, val in enumerate(allDistracted):

        # make a blue and uv snip for all 14
        blueSnips, ppsBlue = snipper(allRatBlue[i], allDistracted[i], fs=allRatFS[i], bins=300)
        uvSnips, ppsUV = snipper(allRatUV[i], allDistracted[i], fs=allRatFS[i], bins=300)
# # these four lines used later to define means plot (made after runs) 
        # Makes a mean for each rat's snips
        blueMean = np.mean(blueSnips, axis=0)
        allblueMeans.append(blueMean)
        uvMean = np.mean(uvSnips, axis=0)
        alluvMeans.append(uvMean)
        
#values for averaged activity for the 2 seconds preceeding (14 values, 1 per rat) =

#TwoSecBEFOREactivity = (np.mean(allblueMeans, axis=1)) # axis 1 gives 14 values, axis 0 gives 1 list of 20 (the averaged average snip)

# Want to produce slices of the lists already here
# I have 14 lists of 300. 0 to 100 are the 10 seconds preding distraction
# 100 to 300 are 20 seconds after 

# Split into (1) 80 - 100 (the 2 seconds before distraction)
           # (2) 110 - 300 (the 19 seconds after - to see if supression)

# JUST BLUE ACTIVITY IGNORING THE UV (NO SUBTRACTION AS PRETTY MUCH ZERO)





allblueMeans = []
alluvMeans = []
for i, val in enumerate(allNotDistracted):

        # make a blue and uv snip for all 14
        blueSnips, ppsBlue = snipper(allRatBlue[i], allNotDistracted[i], fs=allRatFS[i], bins=300)
        uvSnips, ppsUV = snipper(allRatUV[i], allNotDistracted[i], fs=allRatFS[i], bins=300)
# # these four lines used later to define means plot (made after runs) 
        # Makes a mean for each rat's snips
        blueMean = np.mean(blueSnips, axis=0)
        allblueMeans.append(blueMean)
        uvMean = np.mean(uvSnips, axis=0)
        alluvMeans.append(uvMean)
        
plt.plot(np.mean(allblueMeans, axis=0))


# Subset into new lists. Take the snips (preTrial=10, trialLength=30)
# Set to pre trial = 2 (s econds) and trial length is 2 (only before not after)
