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
# Loop through files and calculate burst and run lengths
for filename in TDTfileslist:
    
    file = TDTfilepath + filename
    ratdata = loadmatfile(file)
    distracted = ratdata['distracted']
    notdistracted = ratdata['notdistracted']
    allDistracted.append(distracted)
    allNotDistracted.append(notdistracted)

# ===============================================================================
# ===============================================================================
# ===============================================================================
# ===============================================================================

# Calculating different peaks, and means based on on DISTRACTED and NOT DISTRACTED
# To find peaks and averaged activity across time 

# Photometry figures (individual) for LONG bursts 

for i, val in enumerate(distracted):

        # make a blue and uv snip for all 14
        blueSnips, ppsBlue = snipper(allRatBlue[i], uppqRunTimes[i], fs=allRatFS[i], bins=300)
        uvSnips, ppsUV = snipper(allRatUV[i], uppqRunTimes[i], fs=allRatFS[i], bins=300)
# # these four lines used later to define means plot (made after runs) 
    blueMeanLONG = np.mean(blueSnips, axis=0)
    blueMeans_long_run.append(blueMeanLONG)
    uvMeanLONG = np.mean(uvSnips, axis=0)
    uvMeans_long_run.append(uvMeanLONG)


for i, val in enumerate(notdistracted):

        # make a blue and uv snip for all 14
        blueSnips, ppsBlue = snipper(allRatBlue[i], uppqRunTimes[i], fs=allRatFS[i], bins=300)
        uvSnips, ppsUV = snipper(allRatUV[i], uppqRunTimes[i], fs=allRatFS[i], bins=300)
# # these four lines used later to define means plot (made after runs) 
    blueMeanLONG = np.mean(blueSnips, axis=0)
    blueMeans_long_run.append(blueMeanLONG)
    uvMeanLONG = np.mean(uvSnips, axis=0)
    uvMeans_long_run.append(uvMeanLONG)
