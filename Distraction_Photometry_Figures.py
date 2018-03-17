#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:23:37 2018

@author: u1490431
"""

''' New analysis file for distraction photometry paper, for generating figures
    specific to the paper and adding titles and information to them 

CURRENTLY JUST BARSCATTER PLOTS 
'''

# Imports
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from itertools import chain
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
import matplotlib as mpl

# Defining figure sizes using rcParams 

fig_size = plt.rcParams["figure.figsize"]
print("Current size:", fig_size)
fig_size[0] = 4
fig_size[1] = 5
plt.rcParams["figure.figsize"] = fig_size


# Data processing functions 


# Figure 1
# Long time course figure, lick day 
# Long time course distraction day, with markers added for distractors (in illustrator?) 


# Figure 2
# Averaged distracted vs not distracted (photometry signals snipped)

# Figure 3
# Mean peak height, distracted vs not distracted (VTA)

''' TODO '''

# 1) Simple plot of 30 seconds licking 
# 2) Simple plot of 30 seconds alligned to distractor (not concerned if distracted or not)
# 3) Mark the events on distractor plot 
# 4) Mark licks on / above plots


# JEM function for scatter bar plots
"""
This function will create bar+scatter plots when passed a 1 or 2 dimensional
array. Data needs to be passed in as a numpy object array, e.g.
data = np.empty((2), dtype=np.object)
data[0] = np.array(allData['nCasLicks'][index])
data[1] = np.array(allData['nMaltLicks'][index])
Various options allow specification of colors and paired/unpaired plotting.
It can return the figures, axes, bars, and scatters for further modification.
e.g.
fig1, ax1, barlist1, sc1 = barscatter(data)
for i in barlist1[1].get_children():
    i.set_color('g')
"""
#data = np.empty((2), dtype=np.object)
#data[0] = np.array(examplerat['nCasLicks'][index])
#data[1] = np.array(examplerat['nMaltLicks'][index])


# This data was added manually from excel spreadsheet
# Calculated modelled distractors and percentge from lick data in Python
# Pasted distracted and not distracted into excel and calculated percentage
# Cross referenced against med files and manually entered here:
 
''' Percentage distracted
    Need to add labels and significance stars, either here or in Illustrator
'''
    
percentdistractedLickDay = [0,0,8.33,9.26,0,8.7,1.35,0,4.92,3.23,0,1.33,24]
percentdistractedDisDay = [49.38,81.33,100,42.62,24.32,78.95,10.96,60.94,27.03,57.5,61.11,50,100]
percentdistractedHabDay = [16.13,43.24,100,18.18,15.38,28.95,1.11,18.42,18.75,23.53,21.62,11.76]

distractionData = np.empty((3,), dtype=np.object)
distractionData[0] = np.array(percentdistractedLickDay)
distractionData[1] = np.array(percentdistractedDisDay)
distractionData[2] = np.array(percentdistractedHabDay)



''' Mean flourescence peak (2 second) following distractor or modelled distractor
    
'''
    
''' Mean flourescence peak (2 second) when distracted versus not distracted
    Distraction day only

'''
''' Barscatter '''

colors = ['darkorange', 'orange']
colors2 = ['k','k']
colors3 = ['white', 'white']
 
def barscatter(data, transpose = False,
                groupwidth = .75,
                barwidth = .9,
                paired = False,
                barfacecoloroption = 'same', # other options 'between' or 'individual'
                barfacecolor = ['white'],
                baredgecoloroption = 'same',
                baredgecolor = ['black'],
                baralpha = 1,
                scatterfacecoloroption = 'same',
                scatterfacecolor = ['white'],
                scatteredgecoloroption = 'same',
                scatteredgecolor = ['grey'],
                scatterlinecolor = 'grey', # Don't put this value in a list
                scattersize = 80,
                scatteralpha = 1,
                linewidth=1,
                ylabel = 'none',
                xlabel = 'none',
                title = 'none',
                grouplabel = 'auto',
                itemlabel = 'none',
                yaxisparams = 'auto',
                show_legend = 'none',
                legendloc='upper right',
                ax=[]):
#
#    if type(data) == float
    # Check if transpose = True
    if transpose == True:
        data = np.transpose(data)
        
    # Initialize arrays and calculate number of groups, bars, items, and means
    
    barMeans = np.zeros((np.shape(data)))
    items = np.zeros((np.shape(data)))
    
    nGroups = np.shape(data)[0]
    groupx = np.arange(1,nGroups+1)

    if len(np.shape(data)) > 1:
        grouped = True
        barspergroup = np.shape(data)[1]
        barwidth = (barwidth * groupwidth) / barspergroup
        
        for i in range(np.shape(data)[0]):
            for j in range(np.shape(data)[1]):
                barMeans[i][j] = np.mean(data[i][j])
                items[i][j] = len(data[i][j])
        
    else:
        grouped = False
        paired = True
        barspergroup = 1
        
        for i in range(np.shape(data)[0]):
            barMeans[i] = np.mean(data[i])
            items[i] = len(data[i])
    
    # Calculate x values for bars and scatters    
    xvals = np.zeros((np.shape(data)))
    barallocation = groupwidth / barspergroup
    k = (groupwidth/2) - (barallocation/2)
    
    if grouped == True:
        
        for i in range(np.shape(data)[0]):
            xrange = np.linspace(i+1-k, i+1+k, barspergroup)
            for j in range(barspergroup):
                xvals[i][j] = xrange[j]
    else:
        xvals = groupx
    
    # Set colors for bars and scatters  
#    colors = ['darkorange', 'skyblue']
#    colors2 = ['k','k']
#    colors3 = ['white', 'white']
    
    barfacecolorArray = setcolors("between", colors, 1, 2, data, paired_scatter = True)
    baredgecolorArray = setcolors("between", colors, 1, 2, data, paired_scatter = True)
     
    scfacecolorArray = setcolors("between", colors3, 1, 2, data, paired_scatter = True)
    scedgecolorArray = setcolors("between", colors2, 1, 2, data, paired_scatter = True)
 #   scfacecolorArray = setcolors("between", colors3, nGroups=nGroups, barspergroup=barspergroup, data=dataX, paired_scatter = True)
    
# Initialize figure
    if ax == []:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.tick_params(axis='both', which='major', labelsize=14)
        fig.tight_layout()
    
    # Make bars
    barlist = []
    barx = []
    for x, y, bfc, bec in zip(xvals.flatten(), barMeans.flatten(),
                              barfacecolorArray, baredgecolorArray):
        barx.append(x)
        barlist.append(ax.bar(x, y, barwidth,
                         facecolor = bfc, edgecolor = bec,
                         zorder=-1))
    
    # Make scatters
    sclist = []
    if paired == False:
        for x, Yarray, scf, sce  in zip(xvals.flatten(), data.flatten(),
                                        scfacecolorArray, scedgecolorArray):
            for y in Yarray:
                sclist.append(ax.scatter(x, y, s = scattersize,
                         c = scf,
                         edgecolors = sce,
                         zorder=1))

    else:
        try:
            np.shape(data)[1]
            for x, Yarray, scf, sce in zip(xvals, data, scfacecolorArray, scedgecolorArray):
                for y in np.transpose(Yarray.tolist()):
                    sclist.append(ax.plot(x, y, '-o', markersize = scattersize/10,
                             color = scatterlinecolor,
                             linewidth=linewidth,
                             markerfacecolor = scf,
                             markeredgecolor = sce))

# Explicitly added color here, issue with assignment of scf and sce 
        except IndexError:                    
            print(len(data[0]))
            for n,_ in enumerate(data[0]):
                y = [y[n-1] for y in data]
                sclist.append(ax.plot(xvals, y, '-o', markersize = scattersize/10,
                             color = 'grey',
                             linewidth=linewidth,
                             markerfacecolor = 'white',
                             markeredgecolor = 'k'))

    # Label axes
    if ylabel != 'none':
        plt.ylabel(ylabel, fontsize=14)
    
    if xlabel != 'none':
        plt.xlabel(xlabel)
        
    if title != 'none':
        plt.title(title, fontsize=14)
    
    # Set range and tick values for Y axis
    if yaxisparams != 'auto':
        ax.set_ylim(yaxisparams[0])
        plt.yticks(yaxisparams[1])
       
    # X ticks
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off') # labels along the bottom edge are off
    
    if grouplabel == 'auto':
        plt.tick_params(labelbottom='off')
    else:
        plt.xticks(range(1,nGroups+1), grouplabel)
    
    # Hide the right and top spines and set bottom to zero
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    
    
    if show_legend == 'within':
        if len(itemlabel) != barspergroup:
            print('Not enough item labels for legend!')
        else:
            legendbar = []
            legendtext = []
            for i in range(barspergroup):
                legendbar.append(barlist[i])
                legendtext.append(itemlabel[i])
            plt.legend(legendbar, legendtext, loc=legendloc)

    ax.set(ylabel='Peak ∆F')
    ax.yaxis.label.set_size(14)      
 #   fig.savefig('/Volumes/KPMSB352/PHOTOMETRY MMIN18/PDF figures/Peaks_DisvsNotDis_2sec.pdf', bbox_inches="tight")        
    
    return ax, barx, barlist, sclist
      
def setcolors(coloroption, colors, barspergroup, nGroups, data, paired_scatter = False):
            
    nColors = len(colors)
    
    if (paired_scatter == True) & (coloroption == 'within'):
        print('Not possible to make a Paired scatter plot with Within setting.')
        coloroption = 'same'
        
    if coloroption == 'within':
        if nColors < barspergroup:
            print('Not enough colors for this option! Reverting to one color.')
            coloroption = 'same'
        elif nColors > barspergroup:
            colors = colors[:barspergroup]
        coloroutput = [colors for i in data]
        coloroutput = list(chain(*coloroutput))
        
    if coloroption == 'between':
        if nColors < nGroups:
            print('Not enough colors for this option! Reverting to one color.')
            coloroption = 'same'
        elif nColors > nGroups:
            colors = colors[:nGroups]
        if paired_scatter == False:
            coloroutput = [[c]*barspergroup for c in colors]
            coloroutput = list(chain(*coloroutput))
        else:
            coloroutput = colors
            
    if coloroption == 'individual':
        if nColors < nGroups*barspergroup:
            print('Not enough colors for this color option')
            coloroption = 'same'
        elif nColors > nGroups*barspergroup:
            coloroutput = colors[:nGroups*barspergroup]
        else: 
            coloroutput = colors
    
    if coloroption == 'same':
        coloroutput = [colors[0] for x in range(len(data.flatten()))]

    return coloroutput

# Testing 2D array and barscatter function paired bug fix 
#dataX = np.empty((3,2), dtype=np.object)
#dataX[0][1] = np.array(percentdistractedLickDay)
#dataX[1][1] = np.array(percentdistractedDisDay)
#dataX[2][1] = np.array(percentdistractedHabDay)


# Generate bar/scatter plot for percent distracted incl. modelled distractors
# on lick day and %dis on habituation day 

# (1) Scatter / bar - lick day modelled and distraction day (% distracted) 
# Bars represent mean 
colors = ['darkorange', 'skyblue', 'darkgrey']
colors2 = ['k','k','k']
colors3 = ['white', 'white', 'white']
ax = barscatter(distractionData, paired=True, scatterlinecolor='k', ylabel='Distracted trials (%)')


# Re-define colours, bars, scatter edges and scatter face
#colors = ['skyblue', 'darkgrey']
#colors2 = ['k','k']
#colors3 = ['white', 'white']
#ax2 = barscatter(distractionData2,paired=True, scatterlinecolor='k', ylabel='Percentage distracted trials', title='title')
#

## Data - peak heights for modelled snips and distraction snips (see excel sheet or variables
#    # in photometry analysis script) 
peaksModelledDis = [-0.001217125,0.000859069,-0.001190911,0.036421799,0.008933065, -0.002367187,0.026656246,0.008760555,0.000819196,0.003400855,0.012282488,0.008551392,0.034570625,0.040277452]
peaksDistractorsALL = [0.002176149,0.000233842,0.058384302,0.03030952,0.004967007,-0.002709698,0.04434895,0.008963946,0.017853078,0.036290338,0.035266618,0.041162435,0.040683707,0.051224802]
photopeaks1 = np.empty((2,), dtype=np.object)
photopeaks1[0] = np.array(peaksModelledDis)
photopeaks1[1] = np.array(peaksDistractorsALL)

#
colors = ['darkorange', 'skyblue']
colors2 = ['k','k']
colors3 = ['white', 'white']
ax3 = barscatter(photopeaks1,paired=True, scatterlinecolor='k')

# Need to check where these came from, why are there 21 values?? Subtracted UV from BLUE 
# peaks in first 2 seconds following distractor or modelled distractor 
colors = ['thistle', 'gold']
colors2 = ['k','k']
colors3 = ['white', 'white']
peaksNotDistracted = (0.001005643,-0.000233414,0.047120378,0.039605352,0.005720193,-0.002479069,0.055897022,0.009787216,0.01537006,0.036403637,0.024719976,0.026275861,0.0384651,0.067704732)
peaksDistracted = (0.003363358,0.000194394,0.060783732,0.020370505,0.01726766,-0.003759903,0.041509866,0.012103415,0.019385049,0.036805379,0.042935575,0.050501034,0.074754689,0.042745122)
photopeaks2 = np.empty((2,), dtype=np.object)
photopeaks2[0] = np.array(peaksNotDistracted)
photopeaks2[1] = np.array(peaksDistracted)

ax4 = barscatter(photopeaks2,paired=True, scatterlinecolor='k')


