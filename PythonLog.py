# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:40:12 2017

@author: kp259
"""

'''Log of Python coding and ideas, what was done and when, what needs to be 
   written next. Who's code was used, where resources were found etc.
   
   by Kate Peters'''


'''07/07/17'''
# 15:30 - 16:40
# Worked out how to read in MED file, make data rows and work out total licks
# Wrote code in DIS1_analysis 
# Used JEM code as guide, used "is numeric" function written by JEM
# Next step:
    # Calculate frequency of 3 lick burst - Y
    # Check MED saving format on distraction days (still -22?)
    # Logical indexing and x matrix from metafile
        # Separate by rat over time 
        # Separate by day (group all rats and average)
    # Plot data, histograms, timings of licks - Y
    # Plot mean data across animals 

# Will write all code in full and modularise it to functions / classes later 
# Ask JEM for help with modularisation and looping through cohorts

# 19:40 - 20:00 
# Added 2 lines of plotting, to see how hist works
# Noted to check whether toggle was on in dis1, cannot use onse/offset
# Work out ILIs using diff, wrote instructions for burst calculation

 '''08/08/17'''

# 13:40 - 14:40
 
 # Plotting with matplotlib.plt histogram of ILIs (find most common)
 # Trying to work out lick lengths based on ILIs. Not possible with dis1 data
# Adding text to licks histogram for total licks, customizing

# This evening:
    # Read in metafile, set path 
    # Calculate 3 lick bursts (and mean or median burst length)
    # Calculate longest burst and shortest burst

# 17:30 - 18:10

# Reading documentation for matplotlib
# Edited burstlengthanalysis (JEM) function to include median, check it works 
#with my variables


#Things to consider:
    #Think about exactly what we want to know for the sessions
    # What does normal licking look like?
        # Choice of summary statistic here, is the proportion of 3 lick bursts significantly higher than
            # the proportion of non-3lick bursts? T-test? Multiple comparisons problems?
            # (1 t-test of ALL animals on distraciton-1)
# Note: Use F11, full screen mode less distracting

# Wrote code to calculate non-3-lick bursts, but missing 2%! Need to work out why
    # Maybe single licks not included? Looks like they are
# Fixed the percentage issues (was not using %, was using n of non3Lick bursts)


'''09/08/17'''

# 12:30 - 13:00 
# Read in metafile 
    # !! Problems of multiple variables with the same name (will be fixed when modular) 
    # Looking at how to split lines / read in variables, split strings to make cols
    # How to get data into usable structure
    # How can I index into a list of lists, all the values in position 3 or each list?
    
# 15:00 - 17:30
    # Figured out indexing problem, spliting the strings into character by mistake 
    # Indexed and wrote code to separate out lists into "Rat", "Session" etc. 
    # Unsure how useful, how can I logically index these to get all data from rats 2 
        # Some code to find the index then use that / those indices to index the other columns
        # Seems overly complicated, maybe put them back together but as columns in data frame?

# Created pandas data frame to include all information 
# Trying to understand how mean works in pd.dataframe, odd reuslt when finding mean in column
# ! Realised not numbers, converted to np.array, still need to convert to floats 
# Converted pd array to numeric and found how to avoid NaNs, so far only column by column though

# 20:30 - 21:10

# Looking up cummulative plots
# Writing code to plot cummulative licks 
    # Problems with "height" unsure why
# Trying to fix height issue on cumulative plot
# Found much simpler code with options in hist (and list is fine no need for np.array)
# Figured out how to make line thicker and readable on cumulative plot


''' 10/08/17'''

# 14:30 - 15:30

# Printed and read over existing script, what I have done and what needs doing
# How it works / doesn't work 
# Looking at event plots
# Neatening code, tidying up the way the code looks to explain/understand it better


# Try logical indexing to separate days and rats etc.
    # Wrote code to index rats, need to figure out how to access other column data using the
    # indexes found (for loop or function)
# Writing code to loop through filenames in metafile 
    # Turn medfile reading code into function (like JEM medfilereader)
    # Halfway there, need to remember how to call function bear in mind return 

# 20:10 - 20:30 

# Reverting from function back to code, to test logical indexing
# Indexing not working, error 'series not callable'
    # Same error with both pd.dataframe and np.array 

''' 11/08/17 '''

# 19:45 - 20:30

# Turned on SelfControl for 120mins and Noisli to concentrate
# Fixing function definition after discussion with JEM about returns
# Wrote code to output more than one variable from function;

            #return lickdata, totallicks
            #filename = '/Volumes/KPMSB352/R drive ...' 
            #data, totallicks = MedReader(filename)
            
# Adding start and end assigned variables to MedReader function for readablity
# Changed working directory to find files in for loop 
# Realised it is NOT always -22 (saving structure of MED, has the 26 variables)
    # The distraction programme has many more zeroes, will need to use new code
    # Writing this code, cound n lines, n = value before -2 (saved in MED)
# Making code modular with function definitions and calls
# Problems with logical indexing 

# How to define the distraction with code (not just yes or no)
# More than percent distracted
    # Percent 3 lick bursts
    # Mean post distraction pause vs mean post 3lick burst pause 
    # DPCP vs controls 

''' 12/08/17 '''

# 20:00 - 21:00 

# Reading over code, trying to understand how to fix start:end issue
# Want to access the number in the index, maybe need to conver it?
# Converted using asnumeric within function
    # Error, value error about -3 not in list 
    # Not cutting off at the correct value still, extra 0's at the end 
    # Isolated the code in file 'scratchPadTest' found -3 is at the end of file
# Realised total licks is incorrect for distraction files, not indexed correctly
    # Including zeroes at the end of file 
    # Trying to fix this
    
# Confusion over the index and value, want to find the value in a given index
# Odd values coming out of the indexing, start works correctly, end doesn't

# Think problem is because the index (defined by the number before the -2) is counted
    # From the start, not accounting for the previous numbers cut off for the start

# Got frustrated with it, take a break come back tomorrow    

''' 13/08/17 '''

# 19:30 - 20:10

# Scratchpad file corrupted, all code lost -_- 
# Starting again at trying to fix indexing / value problem 
# Figured out the difference between getting the index and getting the value
    # Realised that it was finding the 492th index from the start of the file 
    # NOT from the FIRST lick value, wrote code to add this in, works!
    # Re-introduce code into original function and test
# Checked that for loop to read filenames from med does access all
    # Checked that MedReader works for distraction and lick training files
        # It does! Figured out how to access just one of the returns from a function

# NEXT
# Figure out the logical indexing, maybe alter the data frame or structure to do this
# Make plots funciton 
# Make PDF outputs for each rat across days 
# Make output of mean distracted and mean 3lick t-test

''' 14/08/17 '''

# 18:50 - 19:20 

# Making plots a function, get it to run through all files in meta (later logical)
# Thinking about the ILIs calculation, includes very long gaps between bursts
    # Want the ILIs wihin bursts only, exclude on a threshold (anything over 0.25)
# Tring to get plotting function and medreader to work together (call reader inside)
# How do you return figures? Function not returning anything
    # Look at Jaime figure function and try to figure out 

# Function works 
    # Remember the difference between return and print is important!

# For loop did the plot funciton for all 152 files, does take a long time 
    # Successfully ran through all files though 
    # Until logical indexinf is sorted comment for loop out (or shorten to one case)

 ''' 15/08/17 '''

# 08:30 - 9:00 

# Logical indexing trying to fix
# Wrote code to separate days, rats and session type
# Errors, noted append does not work on empty list as type none
    # Used + instead to concatenate (for list this works, cannot be integer)
    
# 10:00 - 11:00 (#SUWT)

#Discovered that ctrl+! comments and uncomments!
# Fixed logicla indexing with enumerate, find the logical index of 1 and use 
    # the index of the 1's as indices for the other variables 
    # now trying to add in multiple conditions, if x and y == 1 then give vlaues

# Cleaning up code, making more readable for later interpretation

''' 16/08/17 '''

# 20:00 - 21:00

# Deciding on next steps for analysis
# Altering for loop of logical indexing, maybe don't need a 1/0 column
    # If statement is true the use the index of the true value as index for 
    # desired value in another column, used append here, make new list of distractions
    # for just day 8 (modify to be percent distracted)
    
# Make an average histogram of lick data (get all into one cumulative histogram)    
# Could plot n values of bursts, density of bursts as histograms 

# Day -1 = 7
# Distraction = 8
# Distraction2 = 9
# Saline = 11
# Amphetamine = 14
# Nicotine = 17 

# Figured out how to get means, need to work on plotting these and making function
    # generalised not specific cases
    # test cases for non-distracted days (throw up error or text)
    
# For t-tests, maybe just produce an output of the numbers needed for another
    # stats package to calculate (can work out and then test in SPSS)

# Maybe JEM 'include' column is a good idea here, to limit the lick analysis 
    # to just days that we're interested in 
    
# TO DO : 
    
    # Get 3 lick percentages for each rat on each day, compare in spss each day
    # one way ANOVA with 3lick percentage as measured, day as IV

''' 17/08/17 ''' 

# 16:00 - 16:30
# Writing metaextractor function, modularising code into funcitons
    # consider what the returns will be and how these can be used by other functions 

# Need to consider how to get logical indexing to work with the returned values
    # from the function 

# Tired, took break, considering how best to calculate means and logical indexes 
    # in the most general way possible. Working on testscript2 to run sections 
    # of code before altering main script that works 

# 17:00 - 18:40

# Worked out how to use returned variables in for loop to perform logical indexing 
    # not intuitive looking and confusing
    # consider a better way to do this (names of variables not numerical indexes alone)
        # Maybe return dictionary with keys and not just the multiple variables?

# Writing code to return dictionary of metafile data from metaextractor funciton 
# Working out how to make logical index funciton more general 
    # Thinking about what I actually want to do
        # Get percentage distracted in a list, get non-distracted in a list (info from meta file)

# More important to get the percentage of 3 lick burst into a list and compare
    # Days this way (! For the files identified in the 'DAY' logical indexer)
    # identify the file name 
    # open this file, find 3 lick bursts (make that long code at the end a function and only run on days)
    
# Writing test code in TestScript2 file, looking at optional and named arguments 
    # Writing code for IndexByDay function
    # Do I need a list or code for which days are which treatments? 
        # How will this work for dpcp? 

# Re-insert code into main script, copy from TestScript2 to dis1_analysis 
    # Fixing introduced bugs 


    
''' 18/08/17 '''

# 17:00 - 18:40     

# Fixed data frame, not 'Distractions' = Distractions 
    # Now 'Distractions' = metaDataDict['Distractions'], filling in correct indexes
# Go through all licks, check ILIs and calculate when distracted vs non-distracted 

# Checking 3 lick bursts calculated with the number of distractors given
    # Does not match up
    # Trying to figure out why
    # Less 3 lick bursts than actual distractors given (haven't worked out distracted vs non-distracted yet)
    
# Looking at JEM function 'distractoranalysis' trying to see how it works
    # and if i works with DIS1 (uses timestamps and differences which weren't coded in med here)

# Modifying this function does almost work, clculates distractors as a few too many
# DOES NOT work for distraxted vs not distracted 

# Editing and testing in TestScript2
# Trying to calculate distractors using ILIs in different way (not doubling ILIs)
    # can we compare pairs of ILIs and see if they are > a threshold AND that is a 3 lick burst
        # ie the proceeding ILI was less than burst interval 

# Need to go back to med and see criteria for distractors and bursts, ILIs set in med 

# Inter lick for part of a burst, inter burst and distraction definitions (write these for thesis)

------------------------------------------------------------------------------

''' 19/08/17 '''

# 20:30 - 21:30

# Trying different parameters in distractors function 

# Looking through MED file (MPC code) to see saving format / distraction calculator
    # 3 licks within 1 second 
    # so every 2 ILIs plus every 3 licks must be <1000ms 
    
    # For ILIs find sums of every 2 ILIs 
    # For lick data find sums of every 3 licks 
    # Add these together
        # Will it work?
        # What about long pauses and single licks? May need to do a 3 lick separation first

# Tomorrow, look at the Matlab conversion script and see what needs adapting 
    # Look at key for TTLs and check correct (1 is not)
    # Figure out what the original script does before adapting it 
    
    # Add in doc strings to all written functions (look at Michael's email)
    
''' 20/08/17 '''

# 12:20 - 13:20 # Motivation 4, productivity 4

# Added doc string for main script and doc strings to all functions inside
    # included the purpose of the funciton, arguments expected/required and returns 
    # thinking about arguments and returns from function, esp. plotting functions
    # improving readability of code 

# Still trying to find where the problem with distracted or not is 
    # not categorising correctly

# Brain not working, stuck. Take a break and come back later

''' 21/08/17 ''' 

# 20:11 - 21:20 # Motivation 4, productivity 2

# Making metafile for THPH2, started by checking all data and started to fill in
    # Will add tankfailes when access to R drive more reliable (faster)
# Reading scripts and working out what needs modifying 

# To do:
    # Check THPH1 and THPH2 metafiles are the same
    # Fill in fully both metafules with tanks and info from google sheets
    # Run and edit matlab script
        # Find all functions (like nan etc.) that are needed for MATLAB to run 
        # Start DPCP1/DPCP2 script and metafiles (1 and 2 the same for comparison)

# Added motivation/productivity info to log to see when best times to code 

''' 22/08/17 ''' 

# 11:30 - 12:00

# Trying to figure out this line;
    # doubleilis = ILIs[1:] + ILIs[0:-1]
    # get completely different value if use [0:] in both, why did JEM use this indexing here?
    # Still not right, indexing confusing and double if statement
    
    # changed (y > 1) to (y >2) closer to correct number! 62 if 60 and 87 when 83
        # rationale for changing is the cut off may be 1 second not 500ms 
    # changed   distractedornot = [(lickdata[i+3]-lickdata[i+2]) > 1 for i in distractors]
    # switched 1 for 0.5 (increased n distracted but still not correct!)
    
# 16:30 - 17:30

# MATLAB - switched to look at the tdt2mat2py function 
    # modifying to process the 2 boxes (4 streams, 2 UV and 2 Blue) 
    # writing code to add in second set of data and labelling all with box 2
    # looking over skipping function and others JEM has written, modifying to add second box
    # adding comments to the funciton in new folder
    # changing paths and directories, saving folders etc. 
        # trying to make funciton flexible, make "second box" an optional parameter
        # want to analyse signals ONLY if the stream exists, otherwise just do those that do
    # Labelling of streams has changed no longer Dv1A, now Dv1B, Dv2B, Dv3B, Dv4B (1 and 2 box1)
        # 3 and 4 box 2
    
    # Added in a boxes arg to the function, if ==1 just do as before 
        # If == 2 give both signals 
        # else --> spit out error message and stop (need to add this into code)
        
# To get variable informaiton maybe need to run a single file through ealrier matlab script (TDT2MATBIN)
    # see how everything is named and indexed 
    
    
 ''' 23/08/17 '''

# 9:00 - 11:45

# MATLAB - editing tdt2mat2py function 
# Thinking about how to access data about 1 rat not both in the tank
    # input of function could be changed to give names from both rats, option for 1 or 2?
    # TTLs missing distracted or not TTL?
        # Why? 
    # NB error one is miss labelled (DIS1 missing DID1 is the distractors not distracted or not)
    # output epoch field names to figure out where other 2 TTLs are. Just got rid of ; 
    
       # odd that it is the distracted TTLs (even wrongly named one)
       
    # Load into TDT - check if TTLs exist in the data (read in issue or saving)
    
    # Not a distraction file ! So no distracted
        # need to find out why there is distractors but not distracted in this file
        # look over the tanks (TDT programme on Synapse computer) 
        
# JEM came to look at MATLAB script
# Talked about the distraction script issue with calculating distractors
    # Will now use lickdata rather than ILIs (indexing gets confusing otherwise)
    # Writing code to calculate distractors and distracted or not based on licking data not ILIs
    
 # ---- Break for lunch 

# 15:00 - 16:10

# Calculated lick n+2 - lick n accidentally used ILIs (calculated these incorrectly)
# Need to work this out before calculating distraction 

# Figured out how to get n+2 on the lick data and calculate distractors given, but 
    # 1 distractor out, first? second last? add in condition 
    
# Writing code to work out distracted or not

# Help! Not working

# Number of distractors is one out, either one too many distractors or one less 
# think that is because it misses the last value

# Calculaiton for distravted or not is out, for sme files it is out by only 5 
# seems to add 5 to not distracted and miss 5 from distracted

# For other files (like this one) it is totally out! But total distractors is still only 1 out
    
''' 24/08/17 '''

# 10:40 - 11:30

# Trying to fix distraction script

# Reading JEM comments on script, fixed NDistractors (needed to include the first lick not exclude)
# Now counts correct number 

# Distracted vs not distracted still odd, either completely distracted or strange values!
    # Following JEM advice, checked MED file cut offs, seem to be correct at 1 second   
    
# Checked with another file NDistractors STILL not right, one out for some 
    #files correct for others 

# Special case if the last lick received a distractor? Check this 

# 13:20 - 14:40

# Try appending values to the end of the lists so that indexes don't break (include all numbers)
# Writing code to add zeroes to the end of licks 
    # Did not work

# Writing conditional for if the arrayD index value is less than 4 from the end of licks
    # exclude these values and you cannot do "index+4 if there are not 4 vlaues left
    
# Special case for 1st 3 licks (cannot decide if there is 1 second before ans there is no before) 

# Changed if lickdataNum[index+3] - lickdataNum[index+2] > 0.5: from >1 (must be 0.5) ? NO it's 1
    # not very different between 0.5 and 1
    
# Adding in multiple print statements, checking the indexing and seeing what is 
    # passed from each seciton of code to the next is what I expect
    
    
# 16:00 - 18:00 
 
 ''' Discussion with Jaime over Slack and parallel coding / troubleshooting '''  
 
# Calculated the 4th lick - 3rd lick again, print it before testing the conditions
# Ran up to if statement and printed the non-distracted with each iteration 
# Got rid of if clause after the else (if it isn't <1 it must be >1)

# Checking the addition of distracted/nondistracted in med file (correct)
    # N distractors is right but is the classification of dis vs nondis?
    
# Checked and double checked that 1second was post distractor cut off (and tested other
    #values just in case)
 
# Jaime made raster plot of licks and distractors, I made lick plot with distractors overlaid
    # Aim to see where dodgy distractors are
    # Are they close to a single lick or what is off?
    
# JEM tested Python vs med distracted or not array
# Extracted the distracted or not array from the med file and compared it to Python

# Possibly problem with MED not Python script, it is correctly identifying distractors

# JEM sent code for DistractionRasterFigures, reading over and will test tomorrow

''' 25/08/17 '''

# 12:00 - 13:15

# Meeting with Jaime to discuss MED problem and try to work out solution
# Discussed approach, try running the script with a file from when we had the 
    # timings of the distractors (*med was edited in distraction programme to 
    # create an array of distractor times, THPH1 data is the first to use it)
    
# JEM added in his medreader and isnumeric (returns variables as arrays, a, b, c etc..)

# Manually comapred the timings of the Python and Med outputs

# Python correctly identifying 3 lick bursts and distractors, MED missing some 
# Med ACTUALLY delivering distractors at the wrong time, ocassionally missing 1 or 2 licks
    # 3 licks in 1 second have occurred but med doesn't actually give distractor until next lick
    
# Need to determine HOW this is happening, what is the cut off or threshold for MED
    # missing a distractor? Or delaying it to next lick
    
# JEM looking at this, plotted ILIs and pairs of ILIs, calculated discrepency in excel
    # made raster plots and discussed code of these plots  

# KP to also try plotting the ilis and looking visually at the data 

# Frustrating and confusing. Come back tomorrow morning with fresh eyes

''' 26/08/17 '''

# 20:00 - 20:30

# Looking over DIS1 script

# Need to find alternative method to analyse data from DIS1 and DPCP1 where
    # we don't have the times of the distractors 
    # will be informative once we have DPCP2 data 
    
# Adding code to calculate 4 and 5 lick bursts as well as 3 licks
    # work out percentage of these, added the following code:
    
       #    threeLickBurstsPercent = threeLickBursts/len(bursts)*100
       #    fourLickBurstsPercent = fourLickBursts/len(bursts)*100
       #    fiveLickBurstsPercent = fiveLickBursts/len(bursts)*100
    
       #    fig = plt.figure(figsize=(8, 4)) # Normal, standard size
       #    plt.hist(bursts, bins=50, histtype="step", cumulative='True', color='green', linewidth=2.0)
       #    plt.title('Cumulative HistogramBursts')
       #    plt.show()

# Cumulative percentage plots of 3,4 and 5 lick bursts using histogram func.

# Adapted the lick plots function, attempting to get cumulative plots 
    # think the axes are not right, step function not especially informative
    

# Need to add documentation, fix plotting axes and determine how to get the 
    # correct data on the plot

# Need to shorted and simplify the whole DIS1 script and add documentation 



''' Slack discussion 

1) Average burst length 
2) Distribution of burst lengths. When the distractor is there, 
   even if python isn't detecting it at the same time as med, 
   we would expect this to go down as rats were more distracted

3) Percentage of 3,4 and 5lick bursts, compared to the rest

'''

''' 27/08/17 '''

# 20:00 - 21:00

# Editing lickplots to include all previously made figures
# Temporarily removing for loop (now uses a test case, or set list of test cases)
    # does not make all figures for the entire metafile list 
    # can also fix this by adding an 'include' col and a conditional if include = 1
 
    # Started basic version control by copying dis1_analysis and adding [2] 
    
    # Should look into GitHub and set this up for ease of use later

# Planning next steps to troubleshoot     

# TOMORROW / TUESDAY

# 1) THPH 1 - matlab extraction script
# 2) THPH 1 - Python to accept matlab conversion files 
# 3) THPH 1 - Find Python / Med mismatches
# 4) THPH 1 - calculate correct distraction times (if mismatch check next lick, if mismatch check next end)
        
# 5) DIS 1 - Plotting, fix cumalitive plots
# 6) DIS 1 - statistics, make means as table, info as table, percentages as tables
# Run t-tests in SPSS or Python/R, preliminary result 

''' 28/08/17 '''

# 8:00 - 9:00

# Running THPH1 extraction script to see how it is working or not

# Find cas12 figure script and edit / re-write for THPH1 (and 2)
# Errors in matlab code, look at what cas12cols functions and 
    # cas12 plotting functions are doing
    # what inputs are expected, what are given?
    
# Figure out what the script is doing then re-name and edit everything for THPH1/2

# ! THPH1_2_DataExtractionKP  is the long version of the script (does what we 
    #want to be doing in Python, takes a long time for a single file as extracts
    #everything)

# Remembered why JEM switched to the conversion script
# Need to find out why no distracted if no distractors (but why distractors?)

# Conversion script: TDT2MAT2PY, need to loop through all file paths in metafile 
    # (like Python meta file reader) to get function inputs 
    # trying to remember how to do for loops in matlab and what will be iterated over
    
# Started THPH1_analysisKP script to take matlab conversion files and work with them

# Reading through code in JM_custom_figs and JM_general_functions, for now adding in
    # the functions I need to the script 
    # will eventually make my own modules to import (must be flexible and al purpose)
    # at test stage I want to see everything in the script so debugging easier
    
# 14:30 - 15:00

# Reading through JM_Custom_figs and JM_CustomFunctions 
    # trying to see what I want to do and what JEM has already written 

# Writing list of what outputs are needed from THPH1 analysis 

''' 29/08/17 ''' 

# 12:45 - 14:00

# Discussing the MEd/Python issue with JEM, he identified the problem
# Issue is with MED, counting 1 second 
    # if the iteration or when it returns to the start of counting, happens
    # to be in the middle of a 3 lick burst it will miss the licks which straddle
    # the border 
    
# JEM wrote function to check if the licks have fallen on the boundary / around it 
   # Together editing the script to remove redundant code and neaten it (DistractionCalc2)
   # Writing postdistractionpause function, discussing how to implement this
   
   # Not outputting plot, unsure why - need to give licks info 
   
''' 30/08/17 '''

# 14:30 - 15:30

# Editing JEM_distractionCheckerScript to work without JM_CustomFig etc. imports

# Changing the letter index from JM medfilereader to work with dpcp files 

# Figure out how to do this with dis1 files --> can this be done with dis 1 files?
    # Yes, if we know from the licks when the distractors actially would be (Include the
    # functions that calculate if on a boundary or not) we can back calculate when
    # distracted or not from this

# Looking at changing styles, how to make points transparent, different properties

# PDP - work out if distracted or not, pause over which threshold (check med)                                                                       


# 20:00 - 20:30 

# Adding comments for readability

# Figured out how to add modules to PYTHONPATH with sys.append, add the string
    # of the file location to the search path when importing modules
    
# Deciding convention and names for renaming modules of Jaime's 
    # and putting functions in a logical order within modules 
     # adding clear documentation

# 1) dataproc(for data processing, manipulation, import)
# 2) medfuncs (med pc related functions)
# 3) distcalcs (distraction calculations and processing)
# 4) distplts (distraction plots and figures)

#TO DO:
#    Clean up all modules and add to the names listed above with all doc-strings
#    Move end section of code to dis1/dpcp script (figure out how to read in and 
#                                                  organise dis1)
#    Start dpcp1, analyse data completely 
     
''' 31/08/17 ''' 

# 15:30 - 16:10

# Creating medfuncs, writing docstrings for module and functions 
# Creating dataproc, adding metafile reader and asnumeric functions with docstrings
# Creating distcals, adding functions from JEM and documentations
# Creating displts - looking through own function adn JEM custom figs *

''' 01/09/17 '''
# 20:00 - 20:30

# Working out what needs to be done for results section (very little actual Python, planning)

# 1) Dis1 - get data in (using KP or JEM medreader function, check both)
# 2) Analyse the percentage distracted and not distracted percentage (check same as before)
# 3) Calculate mean post distraction pause (each day, each rat, saved to array)
# 4) Do SPSS statistics 
    #a - ANOVA 1-Way on distracted or not 
    #b - ANOVA 1-Way on mean post distraction pause 
    #c - Make figures, typical licking figure (distracted vs not distracted example)
    #d - Figure, percentage of 3,4 and 5 lick bursts distraction vs normal licking
    #e - SPSS stats, percentage of 3 lick bursts (lick train and distraction) ANOVA
    #f - average figure of some sort?
    
    #g - GraphPad figures, licks, percent distracted, n distractors, post distraction pause
        #g1 - pdp for distracted trials AS WELL as PDP for all trials 
    
# 5) Dpcp1 - get data in using JEM medreader
# 6) Analyse percentage distracter vs notdistracted 
    #a - possible indexing issue, attempt to fix
# 7) Calculate mean post distraction pause (save to an array)
# 8) SPSS statistics
    #a - ANOVA, pcp vs sal (percentage distracted - distracted or not)
    #b - ANOVA, pcp vs sal, mean post distraction pause 
    #c - figure, cumulative licks (normal days) pcp vs sal
    #d - figure cumulative licks 
    #e - figure, frequency of 3,4,5 lick bursts (distracted vs not), PCP vs SAL
        #e1 - compare these percentages using SPSS ANOVA
    #f - GraphPad figures, licks, percent distracted, n distractors, post distraction pause
        #g1 - pdp for distracted trials AS WELL as PDP for all trials

# 9)  THPH1/2 - finish matlab conversion script and run for all files (thph1 and thph2)
# 10) Figure out variable names and streams (may have problem combining thph1 and 2)
# 11) Get same behavioural results as DIS1 and DPCP1
    #a - process in the same way as DIS1, info on licks in bursts etc. 
    
# 12) THPH1 analysis 
    #a) Get the med/py problem fix into THPH script (test)
    #b) Work out distracted vs not and post distraction pause
    #c) Correlation graph between post distraction pause and percentage distracted?
    #d) Allign data to distractors (all) 
    #e) Allign data to distracted and not distracted 

''' Ran some test files through distraction checker, calculated mean and median PDPs 
    looked at plots, concerned over how often (or not) pause is long enough
    
    Will be useful to make plots of ONLY distracted trials, or order by distracted 
    and not distracted, could attempt and then ask JEM about this 

''' 

''' 02/09/17 '''

# 10:30 - 13:30

# Removed code from JEM_distractionCalc module and saved only functions 

# Created final DIS1 script

# Writing fo loop to go through all medfiles listed in metafile and calculate the 
    #Python times of distractors (before correcting with JEM calculation to actual med)
    
# Problem with for loop, want to loop all files and make a distracted array for 
    # each file which is then added to an array of those arrays 
    # currently keeps adding all to one long array with NDistractors being ALL
    # possibly fixed, nested for loop, added a reset for pydis and moved the array 
        #of arrays to the end of the second loop (should equal 152 as 152 files)
        # has calculated distractors on non-distracted days too 
        # edit to exlude these days (need to have an include column or some way to remove)
            # for now, hard coded edit to just start the loop from the distracted days only
            # [56:], working out dictionary indexing to access elements of a list 
            
# Working out how to back calculate the ACTUAL distractor times using the med lick 
    # timestamps and the expected distractor times, with adjustment for the 
    # med problem using JEM py/med comparison 
    
# Adding remcheck, distractioncalc2 and postdistractionpause to DIS1 script
    # writing code to execute these functions on DIS1 data and find actual timings 
    # of distractors 
    
# Trying to figure out the PDP for loop, want to calculate pdp for each distractor
    # array in the array of arraysD (arrayofarrayD, rename this! - theroeticalDisAll)
    # for loop problem again, not correctly updating the pdpALL list 
    # not sure about the indexing here, maybe need to enumerate?
    
# List comprehension index error 
    '''
    pdp = [licks[idx+1]-val for idx, val in enumerate(licks) if val in distractions]
    
    IndexError: index 1290 is out of bounds for axis 0 with size 1290

    '''
# This was a problem earlier with single files, looks like there should be an extra
    #value or a +1 , -1 somewhere? Breaks the for loop as cannot process the PDP
    # re-wrote the list comprehension PDP code as a for loop and added conditional 
        # that value must not be greater than 
# Adding try, except block into the PDP function to avoid index errors / bypass

'''

def postdistpause(distractions, licks):

    try:
     pdp = [licks[idx+1]-val for idx, val in enumerate(licks) if val in distractions] 
     return pdp
    except IndexError:
        pass
    
 '''   

# Noticed pdpAll is offset by 1 as the zero index is the first empty PDP assignment
# May want to go an delete the first or stop it saving the first 
    # For now REMEMBER this when looking for values indexing out by 1  
    
# 14:00 - 15:30
    
            
 # First item in pdpAll is an empty list, all files appart from the first worked
    # try/except has not fixed the indexing issue, just ignored that first one 
    # didn't run the entire thing not just the last index

# Probelm with the try, except block as list comprehension 
    # Converting to for loop, index issues, added in try here and was infinately slow 
    
# Think there is a problem with the multiple for loops
    # Is the pdp function getting the correct inputs on each iteration?
    # the correct licks and distractors? 
    # why is that variable not a global variabel?       

# Function below seems to return the pdp, but only the first one of the list

'''
def postdistpause(distractions, licks):
    count = 0
    for val in licks: 
        if val in distractions:
            pdp = licks[licks.index(val)+1] - val
            return pdp
'''

#TODO
    # 1) Use PDPs to caclulate distracted or not and check against metafile/med
    # 2) Find means and medians of the PDPs in each sublist of AllPDP
    # 3) Export this info to excel 
    # 4) Figure out why allPDP isn't a global variable but adjusted distractors is

''' 03/09/17 '''

# 13:00 - 13:30

# Made new DPCP1 script
# Put JEM medfile reader function in, read in a test file and checked which 
    # letters correspond to which arrays (want lick onset array)

# Checking layout of DPCP metafile, editing metafile reader for headers etc.

# Testing metaextractor and medfile reader on DPCP1 data files with test cases
    # comparing to excel and sheets files. Correct n distractors calculated

# 19:00 - 20:00 
 
 # Checked that adjusted/calculated distractors were the same as meddistractors
     # for dpcp1 files (they are)

# Trying to calculate distracted or not again, using distractors time list and post 
    # distraction pause 
    
# FOllowing code (doesn't work but is closer)
'''
for ind, lists in enumerate(adjustedDistractors):
    for value in lists:
        if value in allLickDataArray[ind]: #if the value is in this list of licks (from all)
            index = allLickDataArray[ind].index(value)
            count += 1
            pdp = allLickDataArray[ind][index+1] - allLickDataArray[ind][index]
    pdpAll.append(pdp) 

# For each index and list of distractors in the whole list of lists (112 lists)
  within the list of distractors for the current file (the current list)for each value
  (each distractor time in that list) 
  
  If the distractor time is in the alllickdataarray list of the same file (same index)
  (otherwise doesn't access the correct licks, goes to the last array of licks)
  Then finds the index of where it is in the licks array for that file
  
  Uses the index to work out pdp
  
  BUT - cannot get it to save the pdps back into lists (which for loop? just lon appended list)
  
  AND - need to fix the try/except issue for index problems or add conditional 
  to exclude the distractor value where there is no PDP (last value)

'''
  
# Realised there is a difference between & and and! Use 'and' for boolean, & is bitwise
  
''' 04/09/17 '''

# 20:50 - 21:30

# Moving for loops around, trying to fix pdp issues
# Writing a work around, indexing / slicing the list into the length of distractors
 
''' 05/09/17 '''
# 20:30 - 21:00 
# Reading through THPH1 script
# To do: 
    # read in data, metafile reader needs editing 
    # check format of metafile (end col?)
    # thinking about differences between THPH1 and THPH2
# Reading about list comprehension (after earlier discussion with JEM about pdp issue)    
 
''' 06/09/17 '''

# 13:00 - 14:00

# Talking about PDP loop issue with JEM
# PDP variable was not resetting inside the loop, so was carrying previous value 
    # back to next iteration and not adding correctly to the pdp list
    # JEM moved pdp assignment into the first loop and it works!

# Looking at the debugger with JEM, seeing how it can be used to mark blocks of code 
    # looking at variables updating as iterations of the loops progress
    # useful to see problems like the pdp one, exactly where the issue is
    # tool can be very useful
    
''' 07/09/17 '''

# 10:00 - 11:00
# Discussing paper stats with JEM (Cas9 data)
# Talking about 2 way ANOVA and t-tests, why post hocs not needed 
# Working out how to get R and Python integration to work 
# Writing code to import csv. into r and getting that code to run in Python 

# Anova produced same results as SPSS and ran from Python with the ro.r command

''' 08/09/17 '''
 
 # Planning only no Python, deed to :
     
#     Add PDP problem fix to the dis and dpcp1 scripts and check it works
#     Add code for distracted and non-distracted
#     Cross check with the information on the excel spreadsheet
#     Produce plots, especially licking 
     
 ''' 09/09/17 '''

# 11:00 - 12:00

# Found method to call R scripts (not commands, but whole scripts) in Python 
# JEM method for calling commands is better, cannot install as admin so work around 
# Useful to perform stats and pass output back to Python 

# Writing distracted or not loop calculator (dpcp1)
# Working out how to store distracted or not for ALL in array (not just for a single test
    # case)    

# Storing values in the loop now fine, but distracted or not is out by a bit 
    # In most cases only wrong by 1, by 1 or 2 sometimes more)
 
# When working out total distractors Python is 1 less for some files, why? This contributes
    # to the incorrect classificaiton but doesn't explain all of it 
 
 ''' NEXT STEPS '''
 '''
 
# 1) Put working PDP code from dpcp into dis 1 (and make a th behaviour only file do the same)
# 2) Figure out total distractors (why sometimes out by 1) 
# 3) Figure out what is wrong with distracted or not calculation (not always out, but often 1 wrong) 
4) Plots
5) Mean and median PDP
!) Indexing by rat and day and treatment 
6) Do spss stats (mean and median pdp) in pcp animals and a measure for dis
7) 3 lick bursts vs rest and distraction day vs last lick day (subset into separate data)

8) Try to run the ANOVAs in R
9) Try to run the R scriptin Python with a useful and storable output 

'''

# 12:30 - 13:30

# Licks is correct and total distractors mostly correct (sometimes misses 1 in Python)
# For distracted or not, timing is over 1 second pause and not over 500 ms (maybe we can classify by this)

# Could do stats with 1 second criteria and 500 ms criteria (can re-run analysis with these 2)
    # mean and median PDPs will also give this information (not binary cut offs)

# Now main issue is the odd occurrence of N-1 total distractors and it takes this 
    # one away from the distracted count always 

# Potential reason: If the distractor is on the last lick (in these 8 files)
# NO, actually if the last distractor is so close to the end that there is less 
    # than 1 second left so cannot classify as distracted or not
    # it looks like MED incorrectly classifies this as distracted 
    # Python does not, it takes away one distracted as this does not meet the condition
        # of licking <1sec or >sec ?
        
# 19:50 - 20:00 

# Adding distractor code from DPCP1 to DIS1 and checking it works
# Verifying with the masterfile that N distractors, N dis or not are correct

''' 10/09/17 ''' 

# 17:00 - 18:30 

# Writing code to calculate mean and median PDPs, storing in array 
    # for each list of pdp's find mean and median and store
    # adding code to both DIS1 and DPCP1 
    
# Adding data to excel sheet, mean and medians ready for data analysis 
    # looking how to do this with Python (automatic making of file)

# Looking at Pandas data frames, converting from data frame to excel is simple
# Writing excel sheets for DPCP1 and DIS1 pdp's means and medians 
# For now add in the file info from metafile manually
    # Attempting to add the metafile info on rat and day to the data frame

# This has worked, used dictionaries to define dataframe and input this to converter
    # Conversion for dpcp pdp data into excel worked, got rid of index col
    # this excel sheet can now be input into R to run the ANOVA (need to define days and PCP/SAL)    
       
# Changing colour scheme in Spyder to dark theme, easier to read 

''' TODO:
    Check the inputs and outputs of the cumulative lick fig function
    Document all funcitons, add to modules, import modules 
    Make plots
    Export data 
    Run SPSS analysis, decide descriptive statistics and summaries, decide
        which programme to use to make plots 
    Write R script for ANOVAs and post hoc T-Tests, figure out corrections
        in R, how to do bonferroni or less conservative correction 

'''

''' 11/09/17 '''

 # 12:30 - 14:30

# Adding variables into excel converter 
# Looking at mean and median PDPs in SPSS (mean is best)

# Add n 3 and 4 lick bursts VS n n lick bursts (all others)
# Editing code and writing new funciton for calculate bursts, lengths of bursts
    # and percentages of 3lick/4lick and other bursts       
    # fixing code, checking that all sum to 100%
        
# Reading through all functions and modules (JEM and KP) checking they work correctly 

# Figuring out what inputs to give for the lick data for DPCP1 (didn't use KP med reader)
    # different means to get at licks (arrays with letters in JEM medfilereader function)
    
# burstcalc function now modified for both DPCP1 and DIS1
# Both scripts output excel file with pdp (means and medians for each file), as well
    # as the pecentages of 3, 4 and 5 lick burst as well as all others 
    
# Next steps:
    
    # Sum of 3,4 and 5 lick percentages, compare with other lengths of bursts
    # Start with graphs, graphpad figures of means (then add significance later)
    # Excel comparison and SPSS, input all data into SPSS
    # Figure out R problem with AOV error term 
    # Decide which descriptives to include and how to order the analysis 
        
''' 15/09/17 '''

# 13:30 - 15:00

# Working out cumulative lick and PDP figures
# Discussing with JEM how to calculate mean and add to cumulative plots
# Wrote code to loop through all liasts of licks and all lists of PDPs to make 
    # cumulative plots
# Need to separate licks and PDPs into:
     # SESSION - lick vs distraction
     # TREATMENT - for DPCP1, saline vs pcp (add both means onto the plot)

# Can do this by making separate lists (manually using the metafile)
    # could figure out the logical indexing and do this Python way

''' 16/09/17 '''

# 10:30 - 14:00
# Subsetting lists in DIS1, extracting licks for the last lick day vs the first
    # distraction day 
# Editing funciton (cumulativelickfig) to take log and scales as optional parameters
# Producing cumulative lick plot for DIS1
    # with mean
# Producing cumulative PDP plot (with log scale) for DIS1
    # with mean 
# Changing aesthetics of plots, font sizes and colours 
# Adding in amphetamine and amphetamine mean, may take back out, not massively different
    # from normal licks and normal PDPs. Commented out for now

# Subsetting lick and pdp lists (more complex than DIS1) 
    # subsetting to lickdaylicksSAL, lickdaylicksPCP etc. 
    
# Producing cumulative lick plots for DPCP1, saline and control 
    # with means for lick day (saline and control)
    # with means for distraction day (saline and control)
    # possibly means for all 4 on one plot? 
# Producing cumulative PDP plot (with log scale) for DIS1
    # with mean 
    
# Writing code (very repetitive) to generate all plots needed for SAL/PCP
# Making all figures for cumulative licks and pdps;
    
LICK FIGURES
    #1 Last lick day SAL (with mean)
    #2 Last lick day PCP (with mean)
    #3 Both last lick day means (sal/pcp)
    #4 Distraction day SAL (with mean)
    #5 Distraction day PCP (with mean)
    #6 Both distraction day manes (sal/pcp)
    #7 All four means, last lick day sal and pcp plus distraction day saline and pcp
    #8 Last lick SAL vs distraction SAL
    #9 Last lick PCP vs distraction PCP
   
PDP FIGURES
    #10 Last lick day SAL (with mean)
    #11 Last lick day PCP (with mean)
    #12 Both last lick day means (sal/pcp)
    #13 Distraction day SAL (with mean)
    #14 Distraction day PCP (with mean)
    #15 Both distraction day manes (sal/pcp)
    #16 All four means, last lick day sal and pcp plus distraction day saline and pcp
    #17 Last lick SAL vs distraction SAL
    #18 Last lick PCP vs distraction PCP
    
TODO:
    
# Decide on the colour scheme to show (1) PCP vs SAL, (2) Lick vs distraction
# Add titles to all plots 
# Save all images and paste them into word at correct size
# Tidy up both DIS1 and DPCP1 scripts  
  
''' 17/09/17 '''

# 20:45 - 21:00
# Copied DPCP1 code to THPH1 behavioural analysis script

# Checking code

# Need to edit all file paths, check file readers and metafile codes 
    # 1) Is the metafile complete and correct 
    # 2) Check column names of metafile allign with the expected names
    
# There is a metafile for THPH2 but not for THPH1
# As soon as possible make metafile for behaviour (exactly the same as DPCP1)


''' 18/09/17 '''

# 10:30 - 12:30

# Made THPH1 metafile, slightly different columns (must change code)
# Editing THPH1 behavioural analysis code 
# Adding correct column names from metafile 

# Problem with burst calculaiton, division by zero?

# Medfile reader, lick array is NOT e, find which is correct
# Lick ONSET data is in array b for these med files 

# Changed the saving folder for excel sheet of information (so does not overwrite DPCP1)

# Subsetting important days, finding indices for last lick day and distraction day
# Subsetting for PDPs 

# Need to exclude rat 1.5 from all behavioural analysis (shorting problem)

# For now, running plots on THPH1, will need to combine
    # work out how to get all data from THPH1 and THPH2 into the same plots
    # at the moment the subsetting works on separate files (could add to metafile)
    # make a combined metafile for the analysis where 2 combined? With column for cohort

# 18:00 - 18:30 

# Decided to merge THPH1 and THPH2 scripts and metafiles together
# Need to move metafile and medfiles to same folder so all can be read
    # change file path and saving 
# Use copied not originals 

# Problems running files, path issue and missing files
    # added in files from R drive (copies)

# Slack discussion with JEM about R and PANDAS data frames 
    # common commands for data frame manipulaitons 

# Checking saving of excel files (DIS1, DPCP1 and THPH PDPs files all saving correctly)


''' 20/09/17 '''

# 8:45 - 9:15

# Finding indexes of last lick day and distraction day for THPH2  to add to the cumulative plots
# Adding indexes to plotting code 
# Making plots for all of THPH1 and THPH2 
# Checked saving to exel file is correct, distraction calculaiton correct 
# Left in files for 2.7 and 2.8 where computer crashed, used backup (not complete) files

# Taking all data saved in excel and putting into graphpad and SPSS
# Making figures for report 
# Doing statistics in SPSS for report 

# COME BACK to python:
    # Running scripts DIS1, DPCP1 and THPH1 and 2
    # Make plot images the same colours 
    # Export (copy/paste) plot images into report results sections / appendices

''' 21/09/17 '''

# 15:15 - 16:16 

# Started THPH(1&2) photometry analysis file 
# Copied medfile and metafile readers over
# Looking through JEM functions, still don't understand classes 
# Need to decide on the output wanted

    # Photometry signals from blue and UV signals 
    # Plots alligned to distractors
    # Plots alligned to distracted VS not distracted 
    
    # What statistics? What quantitative info will be taken from the data?

 # Looking back over MATLAB code, figure out what was done and how the files are saved
 # What is the structure of the output from matlab and how do I index this in Python 
     # How to I get it into Python!?
    
# Trying to figure out what the matlab script is doing and how this translates to Python

# Decided to add to the metafile the names of the mat files for easy looping 
    # Want to avoid using classes if possible 

# Matlab script takes a VERY long time, to do just a single (2 boxes / 1 tank) conversion

# Discussing try/except statement with JEM, problem of different names for THPH1 and 2 
    # For now have to work around the problem 
    # Will run 1 version for THPH1 and separate for THPH2 (2 different boxes as well)
 
''' 22/09/17 '''

# 8:00 - 10:50

# Editing matlab scripts, made 2 tdt2mat2py (one for THPH1 and one for THPH2)
# Two verisons of the looper too?
# Fixing CHAR issue with JEM, running THPH1 script (through all files making .mat)
# Make the saving as outputs and have 2 files from each run of the script (tdt-mat-py)
# Want ideally the same names for referencing on Python
# Writing the THPH2 matlab script, checking if it will run with blank fields in the .txt
# Running converison script (saving all files)

    # For now, script outputs single file with 2 rats in it (need to have separate)
    # Concatenated both rat names into one variable for saving 
    
# Troubleshooting problems, variable names and references, issues of cleared variables 

# Could have matlab save the 2 files or Python interpret the 2 files and split

# REMEMBER THE MISLABELLED TTL (which box? which ttl?)

# Edited indexer for THPH2 to only access every second element in the filenames col
    # (as each file has 2 rats and each second line of the metafile is blank)
    

# 11:55 - 12:10

# Matlab falls down when only one box has been recorded (check this)
# Matlab script missed a file at the end (may be missing from the saved folders)
# Finding the Python script for analysing the photmetry data from MAT files
# Check that the TDT TTL timings will be correct (med issue) should be
# Writing instructions for THPH analysis, what figures for the report and output


# 14:00 - 16:00
# Supervisory meeting and Python   

# WHAT WAS DONE     


REORGANISE FILES AS EDITED DURING MEETING 
Re-index 
Write loop to go through all files and make the plots
Get file path correct 

Add in the UV and blue signals 

Add in the average of all of the signals

Get a peak value (either side of distractor) or post distractor 
Do some statistics

''' 25/09/17 '''

#8:00 - 11:00

# Editing trialsFig code to add second line, one for UV and one for Blue 
# May have some scaling issues
# Noise is a problem, try to use JEM code to remove the noise if possible 

# Noise rmeoval, made bgMAD
# Changing noise thresholds and levels, checking distracted files not lick

# 1.1 and 1.6 look good, may beed to change the threshold each time for each file 
# For now this will work 

# Find the peak in the blue signal (within 5 seconds of the event)
# Store this peak
# Find the same index or same point in the UV signal (subtract or not) JEM uses this

TO DO:
    
# Compare distracted and not distracted 
    # Figure out how to get snips separated by PDP or separated by distracted or not
    
# Get the THPH2 signals into Python, access the 2 uv and blue streams in all 
    # Try to make an average somehow (add up all of the snips from all of the files)
    

# Set up THPH2 reader, the load mat file will need to have 2 sets of extractions
# All plots will need to consider if 1 or 2 boxes and 1 or 2 animals 
# Can actually average all snips as all should be the same length
# Working out how to get maximum value from the averaged trace
    # Limiting this to the first 5 seconds of the snips 
    # Subset the means list, 100:150 will get the means after 10 sec and before 15

# Make a MASTER list of all snips (should have 300 for each rat and each signal)
# THEN get the average from the master list 


# Need to work on looping through files and adding to the master list 
# Make the plots separately though as the scaling factors and noise reduction 
    # thresholds are different ?  

#12:30 - 13:30

# For now, instead of looping (wrote this loop and executed but issues with scales)
    # will manually execute the file and adjust parameters before saving images
    # will fix this later but now just need files and numbers 
    # manually take the max number from each iteration and add into excel/spss
    
    # do this for all 6 THPH1 and all 8 (2 at a time with adjustable plots and noise)
        # THPH2 

# 14:40 - 16:30    
# Work out how to add all the snips to a mean list for making a master figure 

# Manually producing and adjusting figures for THPH1 
# Reading in THPH2 files, checking the array to see naming of distractors and licks
    # and uv/blue streams, looking at TDT_TTL key 
    # realised I used distractioncal2 to find distractors, no need for the TTLs
    
# Editing code to take 2 boxes, adding 1 and 2 to figures and making second set
# Trying to loop but difficult as too many different noise parameters 

# Averaged all averaged snips (blue and uv) manually input into excel 
    # Average figure could be EVERY single trial
    
    # Find a way to re-import the manually saved data from excel (the averages)
    # Make plot of average of averages! With all averages on the plot and 2 bold
        # "master averages"
    # Changing data types so that TrialFigs will accept the averages
        # need to give it as lists not as separate keys in dictionary
        # did it the long way round, made whole figure from scratch
            
     
# LATER TO DO 
# Writing funciton to separate out distracted (could use the array in this case for THPH2)
# Trying manually first then resort to array after

# May need to multiply everything by pps? May not (did not with distractors)
# Not quite working, not saving any distracted's (will need to do it manually for THPH1)

# Automatic methods works for THPH2 (cross-referenced against metafile and med)

''' Think about:
    
    How do I access NOT distracted? Have the distracted times (simple way to 
    access the rest)
    
    Work on making distracted plots for these 6 animals (if not very distracted may have issue)
    
    Work on total manual calculation (without TTLs)
    
    Heat maps?
'''

''' 26/09/17 '''

# 9:30 - 11:00

# Running distracted separated files
# Working out and writing code to find non-distracted from the distractor and 
    # distracted arrays (from TDT)
    
# Writing code to compare all distractors with distracted (need to -1 from distracted)
    # as this is determined 1 second after
    # beware of rounding! Decimal place numbers are not the same for the 2 lists
    
# Finding indexes of distracted and not distracted 
# Using loop within function to access the indexes of the distracted and non-distracted

# Figuring out how to get the for loop into the loading sesison funciton and re-writing 
    # code to make separate function for "nondistractedIndexer"

# Separating out by distracted and not distracted done, need to make the plots
    # and get the numbers out 
    # make sure all of the noise functions are adapted for the new plots
    # check all calculations 
    
    
#12:00 - 14:25

# Make plots (representative) and means for lick days (check there are no peaks)
# Making the plots (3 files to run through and change parameters)
# Try first keeping the parameters the same for distracted and not
# Got rid of 2.5 as massive peak (probably artifact, looks too strange)

#13:10 - 

# Adapt code to make a figure of distracted and a figure of not distracted
# Could play with having these on the same plot if possible 

# Check the peak calculations and add to the excel sheet

# If want to add the blue signals to the same figure (distraced and not) complicated
    # need to efit the snips and noise (use same noise calc)
    # change trialsfig function to take different inputs OR give it 2 blue not UV
        # if giving 2 blue change the colour to different blue 

# Adapting code to allow 4 sets of "snips" per box 

# Making averages for distracted and nondistracted  
# Added these 2 averages to one plot of just the blue signals 

# Manually exporting ALL numbers, means from uv and blue to see difference 
# Could calculate absolute blue peak and blue peak normalised agains uv


''' 04/10/17 '''

# 17:00 - 19:15

# Editing photometry script
# Make script work for simpler MAT files (now each rat/sesison has 1 file)
# All files have the same variable names (JEM updated metafile and exported all mat)

# Writing funciton to manually calculated distracted or not 
# Look at list of distractors given and calculate if they are distracted or not 

# Changing file paths to the R drive (copying test files) - new MAT structs

# Writing distractedornot funciton, outputting only one value not the whole times list

# Need to go back and work out the PDPs and whether distracted or not from these
# Decided to do the whole thing manually ignoring the distracted/not ttl


# Give funciton list of distractors and list of licks 
    # Sanity check that distractors do appear in licks 
    # Find where distractors appear, get the index
    # Get the index plus 1 and subtract to get that indiviual PDP
    # If the PCP is over 1 second add the distractor time to distracted 
    # If the pdp is less than 1 second add the distractor time to the non-distracted list 

# Done, distractedOrNot function works 

# Need to:
    Check metafile reader is correctly set up 
    Add or make a .csv to go through the THPH .mat files (names for looping)
    Start looking at the noise issue 
    Start writing a PDF saver for when the noise issue is sorted
    Check the trialsFig function and other of JEM - the one with classes "makephototrials"
    
n.b saved as PythonOct in KP259 on R drive (Python current) as cannot save to shared drive


''' 05/10/17 '''

# 16:30 - 18:00
# Tidying code, trying to get noise functions to work
# Editing plotting and changing parameters of noise functions / calculations
# Don't know how it works and why it isn't doing whatI want it too
# 

''' 08/10/17 '''

# 18:00 

# Changing file paths so functions can find metafile and individual MAT files
# Checking plotting works correctly (change colours)

# TO DO:
    # Make all figures for each rat on last lick day and first distraction
    # And for distracted and not distracted
    # Save these in word and then make PDF for JEM
    # Add info on percentage distracted and mean PDPs
        # Get this to print with the plotting outputs
    
    # Get numberical information on peak, max value in first 2 seconds from 
        # the generated plots (with the new noise remover working)
        
    # T-test compare: LICK DAY vs DISTRACTION (normalised against the UV)
    # T-test peaks DISTRACTED vs NOT DISTRACTED 
    # Access individual trials and plot these (see each snip and pick representative)
    # Allign all to " first lick " in a bout or burst (nothing 10 seconds preceeding)
    
 ''' 09/10/17 '''

# 7:30 - 9:00

# Editing excel file, making peak heights and means by running script multiple 
    # times with different rats
    
# Sheets for lickmodel, lickalligned, distractors, distracted, notdistracted 
    # and peaks
    
# 19:00 - 21:30 

# Completing excel sheets, finishing getting 2 seconds peaks (and subtracting UV)
# Running all distractors plots and numbers (not saving plots looking at them)
# Saving all uv and blue means to excel spreadsheet 

# Running plots and statistics for means (to send to JEM and finish abstract)

# Compiling complete spreadsheet, saving as separate .csv files with paths 
    # commented in/out for easy access 
    
# Re-did all t-tests in R commands below : 
    
''' 

lickdaypeaks = c(-0.001217125,0.000859069,-0.001190911,0.036421799,0.008933065,-0.002367187,0.026656246,0.008760555,0.000819196,0.003400855,0.012282488,0.008551392,0.034570625,0.040277452)
distractionpeaks = c(0.002176149,0.000233842,0.058384302,0.03030952,0.004967007,-0.002709698,0.04434895,0.008963946,0.017853078,0.036290338,0.035266618,0.041162435,0.040683707,0.051224802)

distractedpeaks = c(0.003363358,0.000194394,0.060783732,0.020370505,0.01726766,-0.003759903,0.041509866,0.012103415,0.019385049,0.036805379,0.042935575,0.050501034,0.074754689,0.042745122)
notdistractedpeaks = c(0.001005643,-0.000233414,0.047120378,0.039605352,0.005720193,-0.002479069,0.055897022,0.009787216,0.01537006,0.036403637,0.024719976,0.026275861,0.0384651,0.067704732)

t.test(lickdaypeaks, distractionpeaks, paired=TRUE)

t.test(distractedpeaks, notdistractedpeaks, paired=TRUE)



'''

''' 09/11/17'''

# 12:10 - 12:30 

# Working on Github repository, figuring out files and how to commit edits
# Need to make repositories for each project 


''' 01/02/18 '''

# 4-5pm

# Reading through all scripts (THPH) and trying to figure out what 
# they do and where the data are saved, where files are created etc. 

# DPCP - what is the status of this?
# THPH - How have I combined 1 and 2 ? What is the status?
# NAPH - what needs to be modified? Is there a universal style metafile?


''' 02/02/18 '''

# 9:00 - 9:30

# Changed (and added) filepaths for PhotometryAnalysis script 
# Found data files (mat files already converted for final lick days and 
# distraction days)

# Ran PhotometryAnalysis script, produced output! Means I have calculated 
# previously and stored as .csv files

# Should double check what each of these "means" files corresponds to
# Check how peaks are calculated

# Attempted to run THPH1and2_Brhaviour on Mac, uses R drive (must run from 
# university PC, or add filepath to R drive copy on memory stick or Mac as option)


''' 05/02/18 ''' 

# 19:00 - 20:00

# What does the analysis code actually do?
    # (1) Assigns a data folder 
    # (2) Assigns an individual data file in that folder 
    # (3) Loads the equivalent matlab file (which produced dictionary of relevant cols)
    # (4) The load matfile calculated distracted or not from TTLs in Synapse
    # (5) Takes blue and UV snips around TTLs of designated event (not distracted, 
       # or distractions or distracted etc... could use licks here?)
    # (6) Makes random events to create a noise index for later removal
    # (7) Makes a trials figure (for this example, individual rat) all data
    # !!! So far all for a single rat, later the script uses means which I manually 
        # calculated for each rat and added to separate .csv files      
    # (8) Makes trials multishaded figure for this rat, has error bars and uses a mean
    # (9) Makes array of maximum peaks - within a given time range 
        # later used (or previously after manually saving .csv) to make average figures
        # across multiple rats 
    # (10) Print maximum value in 2 seconds following distractor or distraction 
        # for blue channel and UV channel (based on maximum value within time)
        
    # (11) Using means files (created for different featires, ie. distracted, nondistracted)
        # plots on aggregated data for all thph1 and 2 rats with observations on the 
        # distraction day (and preceeding lick days)

# Next steps: Produce and save figures
# Make a mult shaded figure for the means 
# Automate the adding columns to .csv files for the means and for each "examplerat"
    # Need to use the metafile to run through filenames and get data from all rats
    # process, extract infor and then save columns and figures generated 
        
# Thinking about how to make longer time course figure from existing functions
# Extend the time of the snipper?

# Main output is a means figure, of distracted ot non-distracted trials 
    # has all data and not error bars 
    
# Created new script file to work on figure generation 
    # Laid out the figures to include, what they should be and some basic code

''' 08/02/18 '''

# 21:00 - 21:30

# Wrote code to make longer timecourse plot
# Some issues with scaling and old data staying on new plots
# Possibly worked for the first plot?

# Wrote to do list of three simple plots to tackle tomorrow 

''' 09/02/18 '''

# 10:30 - 11:30 

# Trying to figure out how to allign plot so that "event" is the first lick 
    # in a bout of licks 
# Reading through previous scripts where calculated first lick in bout 
# Trying to edit plot code and snipper to create events from licks (TTLs) when 
    # meets condition of X licks in a run 
    # store the licks which start a run or burst, so they can be input as "timelock"
    # parameter in Snipper function 
    
 ''' sessiondict['lickRuns'] = lickRunCalc(sessiondict['licks']) ''' 
 
 # Need to write lickRunCalc function that takes an array of licks and finds 
     # the start of bursts or runs
     # 1) Define burst or run 
     # 2) For each lick add to the store/list/array if it is followed by more 
        # than X licks within X ms/sec
    
# Work in progress, writing function for lickRun / burst calculation 
 
def lickRunCalc(licks):
    
#    distracted = []
#    notdistracted = []
runstart = [] 
    for lick in licklist:
        runstart.append(l)   

    for index, lick in enumerate(licks):
     
            try:
                if (licks[index+1] - licks[index]) < 1:
                    and if (licks[index+2] - )
                    
                    ?
      # if there are more than 5 licks after this index (ignore the last 5?)
              
                    
                    distracted.append(licks[ind])
                else:
                    if (licks[ind+1] - licks[ind]) < 1:
                        notdistracted.append(licks[ind])
            except IndexError:
                print('last lick was a distractor!!!')
                distracted.append(licks[ind])

    return(distracted, notdistracted)


# Looking at function from Murphy et al (2017)
'''
"""
This function will calculate data for bursts from a train of licks. The threshold
for bursts and clusters can be set. It returns all data as a dictionary.
"""
def lickCalc(licks, offset = [], burstThreshold = 0.25, runThreshold = 10, 
             binsize=60, histDensity = False):
    
    # makes dictionary of data relating to licks and bursts
    if type(licks) != np.ndarray or type(offset) != np.ndarray:
        try:
            licks = np.array(licks)
            offset = np.array(offset)
        except:
            print('Licks and offsets need to be arrays and unable to easily convert.')
            return

    lickData = {}
    
    if len(offset) > 0:
        lickData['licklength'] = offset - licks
        lickData['longlicks'] = [x for x in lickData['licklength'] if x > 0.3]
    else:
        lickData['licklength'] = []
        lickData['longlicks'] = []

    lickData['licks'] = np.concatenate([[0], licks])
    lickData['ilis'] = np.diff(lickData['licks'])
    lickData['freq'] = 1/np.mean([x for x in lickData['ilis'] if x < burstThreshold])
    lickData['total'] = len(licks)
    
    # Calculates start, end, number of licks and time for each BURST 
    lickData['bStart'] = [val for i, val in enumerate(lickData['licks']) if (val - lickData['licks'][i-1] > burstThreshold)]  
    lickData['bInd'] = [i for i, val in enumerate(lickData['licks']) if (val - lickData['licks'][i-1] > burstThreshold)]
    lickData['bEnd'] = [lickData['licks'][i-1] for i in lickData['bInd'][1:]]
    lickData['bEnd'].append(lickData['licks'][-1])

    lickData['bLicks'] = np.diff(lickData['bInd'] + [len(lickData['licks'])])    
    lickData['bTime'] = np.subtract(lickData['bEnd'], lickData['bStart'])
    lickData['bNum'] = len(lickData['bStart'])
    if lickData['bNum'] > 0:
        lickData['bMean'] = np.nanmean(lickData['bLicks'])
    else:
        lickData['bMean'] = 0
    
    lickData['bILIs'] = [x for x in lickData['ilis'] if x > burstThreshold]
    
    lickData['bILIs'] = [x for x in lickData['ilis'] if x > burstThreshold]

    # Calculates start, end, number of licks and time for each RUN
    lickData['rStart'] = [val for i, val in enumerate(lickData['licks']) if (val - lickData['licks'][i-1] > runThreshold)]  
    lickData['rInd'] = [i for i, val in enumerate(lickData['licks']) if (val - lickData['licks'][i-1] > runThreshold)]
    lickData['rEnd'] = [lickData['licks'][i-1] for i in lickData['rInd'][1:]]
    lickData['rEnd'].append(lickData['licks'][-1])

    lickData['rLicks'] = np.diff(lickData['rInd'] + [len(lickData['licks'])])    
    lickData['rTime'] = np.subtract(lickData['rEnd'], lickData['rStart'])
    lickData['rNum'] = len(lickData['rStart'])

    lickData['rILIs'] = [x for x in lickData['ilis'] if x > runThreshold]
    try:
        lickData['hist'] = np.histogram(lickData['licks'][1:], 
                                    range=(0, 3600), bins=int((3600/binsize)),
                                          density=histDensity)[0]
    except TypeError:
        print('Problem making histograms of lick data')
        
    return lickData    
'''
# TODO:
    
# Start looking at whether you need onset and offset or whether onset is enough 
# Read through the code and see how it works 
    # threshold for bursts can be set
    # is there a more simple way of doinf this?
    # which bits of the function stop the index errors?
    
    # What is the output? - Start, end, N licks for each burst
        # Useful to store this, but only want to acess the start of the burst, the
        # first lick to allign all photometry signals in distraction and lick day data 
# ! will need to add lick offset to matfile loader if want to use this code as is

    

# 14:00 - 15:00 Supervisor meeting 

''' 13/03/18 '''

# 9:20 - 10:20 

# Reading through THPH1 and 2 behaviour analysis 
# Will add licking structure analysis here? Or use the TTLs from TDT?

# File runs (changed filepath to HDD) and produces cumulative licking plots 
    # Can take some of these for the poster for MMiN18 
    # Start compiling "behaviour" only figures and deciding which to include in paper

# This file plots the cumulative licks for licking day and distraction 
    # plots each rat (across whole session) and an average for both days

# Also plots the cumulative PDPs - post distraction pauses 
    # for lick day and distraction day (modelled distractors in the case of lick day)

# Paused Python for a bit, looking through results and writing some of the section

''' 15/02/18 '''

# 08:30 - 10:11

# 1) Behaviour
            # Using just MED files to start 
            # Produce the PDP plots, format them and export 
                # Decide on colour scheme, kelly green and greys/blues
            # Make percentage distracted lick day average plot, distraction day plot 
                # Add in habituation day too
                # Add in the circles and lines from each point (rat across days)

# Trying to calculate percent distracted from modelled distractors 
# Issues with divisions 

# Uninstalling and re-installing conda a million times on UOL client -_-

# Found that I manually calculated percent distracted by copying and pasting 
    # the distracted and notdis arrays into excel, checking against the med values 
    # and using formula in excel!
    # re did this and got the same result as the previous data found in Prism
    # now --> input this into arrays and make JEM scatter/bar plot            
            
# Making barscatterplot
    # In script "Distraction_Photometry_Figures
    # Need to figure out how the "set colors" and other functions work with 
        # this plotting function
    # Cannot see how to add in the lines between scatters
        # thought it was in the paired=True lines but nothing changes when I alter
        # looked like the paired=False was always triggered, and the else never
            # commented out and just ran the else, still no lines! 
            # Ask JEM in meeting Friday!!

''' 16/02/18 '''

# 10:20 - 11:00

# Start burst / cluster analysis 
# Confused about what the dictionary output contains, and how to plot the burst lengths

# for the start lick of each burst (or run?)
    # find the interval to that lick minus 1
    # and the interval to that lick plus one 
    
# Why is burst time (the length in time between start and end of burst) so short?
# How can there be just 1 lick in a burst?

    # Maybe need the lick OFFSET values too? (might need to alter loadmatfile)
    # If this is the case will the function work?
    # Why does it not plot histogram? How does np.histogram actually work?
    
  sessiondict['licks_off'] = a['output'].licks.offset

# Added offset to matfileloader dictionary output to pass into the LickCalc func
  # Still produces output with bursts of 1 lick (how and why?)
  # maybe I need to limit the code to only record bursts of 3 licks or more? 
    # or just exclude the 1 lick "bursts"
    # or use the runs? - Not high number of runs though (<10)

#!! Possible this rat didn't lick a lot --> 357 licks (with 320 of those in one long run)
# perhaps this rat is not typical, check another rat with more licks 

# 15:00 - 16:30 
# Supervisor meeting with JEM 
#
# Discovered bug with bar scatter plot
#•	Reason I couldn’t get the scatters to be paired
#•	Function set up to expect 2D not 1D array
#•	Ie. Like excel sheets with groups on each sheet etc.
#•	Will work as it is for grouped data but not for what I want to input
#
#•	N.B  → To assign a 2D array (like an array of arrays)
#•	[[1,2,3],[1,3,2],[1,3,2]],[[1,2,3],[3,2,4],[4,5,5]], etc...
#•	Large is the “sheet” or layer, small is the column within the sheet 
#
# Looked over other functions and discussed 1D and 2D arrays
#•	Data2obj1D and data2obj2D
#•	Single list into object array or 2 lists into 2D array (could combine these)
#
# Working on bar scatter
#•	Writing code to check the shape or dimensions of input data
#•	How to extract each value from the same index in the 3 lists in the array?
#•	List comprehension
#
# N.B Don’t forget to test all conditions of the function, each possible execution (pass in a 2D array to check it works with this)

''' 18/02/18 '''

# 20:00

# Added colours for scatter back into the code
# Issue with color section - 'scf' no assigned yet 
    # Assigned in the if statement when paired is false
    # Try adding explicit colours first then adding assignment 
    
# Making a 2D array - figuring out how to do this and what it represents 
    # Testing function with 2D array 
    # It works!! If enter groups as "sheets" in the 2D array the pairs are correct

# Looking up hex code colours, like golden yellow and sky blue together for figures
    # Maybe 2 blues and 2 yellows/orange with light and dark greys together
    # Then poster colour can be nice sky blue 
    
''' 19/02/18 '''

# 14:00 - 15:15

# Working on lick calc and with the dictionary output
# Trying to figure out why the histogram has no output  
# Got it to make plot output, but now histogram superimposed on previous figures
    # How do I stop it doing this???
    
# Python keeps track of current axis, and plots to this (pyplot)
    # Made new axis and defined properties 
    # Histogram now plotting correctly
    # Doesn't look particularly informative --> need to adjust bin sizes
         # Not sure why one bar is blue and why not equal spacing?
         
    # Maybe order the bursts by length and plot these (not freq, individual)
        # sortedBurstLen = sorted(burstanalysis['bLicks'])
        # plt.plot(sortedBurstLen)

# Sorted list looks like cumulative plot! Shows there are quite a few 1 lick 
    # bursts and 1 lick runs!
    
# Trying to figure out how to calculate bin sizes and bins 
     # Not enought bins, confused why does changing bins change the y axis?
     # No change to X?
     
# Weird multicolour histograms, plotting 2 data sets? 
     
''' 20/02/18 '''

# 10:00 - 11:00

# Jaime explained histogram issue, defining it twice
# np.histogram gives the edges and I was plotting this as well as the hist

# Re-wrote histogram code
     # figure12 = plt.figure()
     # NOT NEEDED --> a = np.histogram(percentdistractedLickDay)
     # plt.hist(percentdistractedDisDay)
     # plt.show()    
    
# Mode
    # Mode is 1 for runs and bursts, why are there bursts and runs of 1?
    # Look over the code and fix this, maybe add a "must be over 2 / 3" clause

# Thinking about making new logs, for each month. Start in March with MarchLog 
# Change this file name to ArchiveLog or HistoryLog

# Changing definition of RUN, making the pause smaller to see how many runs we get
    # Want a long enough pause before the run to plot what happens before (without another run/burst)

# Could define the interval before as from 1st lick in the burst to distractor?
# Or find some way to differentiate intervals before by s,m,l?

# Thinking about how to measure the interval before the burst if I set a 
    # cutoff for runs in the LickCalc function as 2,5, or 10 seconds 
    # maybe look at the bursts (no definition of run here)?
    
# 0.5 --> cluster
# 0.25 --> bursts?     

# Interval after a 1 lick burst? Correlation between the post inter-burst interval 
   # number of licks in the next burst 
   
   # for every burst work out the interval and plot the 2 against each other
   # do these 1 lick bursts always come a little before a long burst?
   # if there is a short interval is the burst length longer or shorter?
   # following a long burst is the interval longer?  
    
''' 26/02/18 '''

#

# Need to make a list and go through it of plots, start with scatter bar plots

# Then move on the behavioural, save as PDFs and save the script in figures (in order)
# Licking analysis and pauses etc. in behaviour (and stats analysis, export numbers)
# Then photometry, distracted versus not
# Licking bouts photometry    

LIST

''' 27/02/18 '''
# Testing JEM GUI and looking over code
# Giving suggestions for features and testing with different files 

''' 01/03/18 '''

# 17:15 - 18:00

# Looking at poster layout and checking which plots are needed
# Need to make :
    
    Licking plots for behaviour 
    Means?
    Distraction behaviour plots
    Photometry licking 
    Photometry distractors
    Photomtery - modality??
    Photometry distracted 
    Heatmaps??
    
# Added comments in Distraction_Photometry_Figs. to scatter bar to make 
    # other figures for paper/poster
# Finding date for peak values (old script and excel sheets previously made)

Results
1) Rats pause ongoing licking following distractors 
    # Percentage distracted - just show modelled and distraction day
    # Post distraction pause - increased pause following distractors vs model
    # Cumulative PDP plot - difference between normal lick day and distraction day
    
2) 1 Behaviour - Licking, burst/cluster/run
   Relationship between pre-bout pause and burst/run/bout length
   
   # Plot of pre burst pause and burst length 
   
3) Bout length predicts distracted or not?
4) PHOTOMETRY - Licking peak, just lick day 
5) Scatter of lick burst length and peak magnitude
6) Scatter of pre-burst pause and burst length 
7) Scatter of pre-burstpause and peak magnitude on first lick?
            
? Arbitrarily decide short, medium, long pauses (based on histograms)

''' 02/03/18 ''' 

# JEM MEETING 14:30 :

# How to isolate a single trial from photometry data and plot it?
    # How to plot every trial as one plot from TDT data only 
        # How to overlay distracted or not AND licks (TTLs) onto the plot 
            # Or as a separate plot I can 
            
# See meeting notes for info on individual trial plots using FindNEarestEvent 

# Want to plot each trial alone, separate by distracted or not 
# and add the licks TTLs as markers on the plot 
# graphical way to explain distraction trigger/distracted etc.
# and raw data plot example. 

'''
triallicks = nearestevents(examplerat['distractors'], examplerat['licks'])

trial = 7

f = plt.Figure()
ax = plt.subplot()
ax.plot(blueSnips[trial])
ax.plot(uvSnips[trial])
xvals = [(x+10)*10 for x in triallicks[trial]]

yvals = [ax.get_ylim()[1]] * len(xvals)

#ax.scatter(xvals, yvals)

ax.scatter(xvals, yvals, marker='|')

ax.plot([100,100], [ax.get_ylim()[1], ax.get_ylim()[0]])

'''

# Remember, found the ylimits to plot the scatter and defined the marker 
    # to mark licks 
    # had to also scale the actual values to the -10 to 20 scale of the snips
    # this is done using the constant and expression: (x+10)*10
    

''' 05/03/18 '''

# 13:30 - 14:10

# Looking over Friday's python individual plots

# Lick plots:
    # Lick day descriptives
#            a) Average burst lengths, licks per burst median etc. 
#            b) Photometry, align to start of a burst (all)
#            c) Photometry align to start of burst by top 25 and bottom 25% of lengths
#            d) Pre-burst pause (short and long) topand bottom quartiles
        
            
# Slack discussion with JEM 
# Deciding how to represent mean/median data, whether to look at mean/median 
    # burst lengths for each rat and then show the mean of all 
    # or to rank all data and find mean median from grouped 
    # decided for stats use INDIVIDUAL RATS and then mean/median
    # for histogram plotting use ALL RATS TOGETHER (frequencies of different
        #burst lengths for all of the rats as a cohort on the last lick day)
    
   # Similar idea for the upper and lower quartiles 
       # Want to define high and low number bursts
       # Do both --> quartiles for each rat and quartiles for the whole data set
       # Then see which looks best 
       # Probably end up using the whole data set together (more reliable less noisy)

# Writing Python list for figures, making step by step plan to get Licking figures
    # finished by Friday and then the distraction figures ASAP

# 14:30 - 14:50

# Adding in code to have licks, distractors and distracted or not on the same plot
# figuring out how to get them at different Y levels on the plot 
# add constant to the "getylim" line (small signals, small scales, small constant)

# Tested this on a LICK DAY
    # need to make these plots for distraction days individual trials 
    # can compare to the last lick days if wanted 

# How easy would it be to change the size of the snips? --> re-scale later plots
    # shorter time course for looking in detail at the distracted or not and licks 
    # around 5 seconds either way 
    # although longer for the pre-burst pause info

''' 07/03/18 '''

'''
for each rat (or file) in the list of files - make list
    open the file
    run the example rat script 
    extact the licks
    calculate the burst lengths
    add the bLicks and rLicks to a master list (append each list to
                                                the master)

Then using master list, make a histogram of all the lick bursts from 
all the rats      

'''

# Writing new script to make the plots, reducing unecessary code 
# Start with the histogram 

# Wrote for loop to go through 14 files (the 14 last lick days, N/B
    # for distraction there are 12 as 2 did not have this day) 
    # loads the matfile and produces the disctionary for each rat

# Putting the lickCalc / burst analysis into the loop to get a list
    # of burst and run lengths for each rat
    # writing loop to append - remember issues with PDP loop similar

# Half working, appended each array to the list 
    # want one continuous list / array NOT 14 lists ?
   
    # Maybe not append, take the burst list (which is an array) and add it
        # to the end of an empty array? Try making empty array not list

# Used itertools and merged the lists in the list, simpler than either list
    # comprehension or for loop 
    
#TO DO
# Add means/medians to plot 
# 1) Means and medians from ALL aggregated
# 2) Means and medians from EACH RAT then averaged  

# Could add N burst too, the mean N burst and mean N runs 
# Check the definitions of runs and bursts and see if JEM has different cut
# offs

# In future, have all functions in one long file and then run this first
    # gets around issue of needing packages or modules 
    # will make code much more readible

''' 08/03/18 '''

# 08:30 - 10:00 

# Change bin sizes of histograms to see if more informative
# Change x-limits and see if you can zoom in on histogram / make clearer
# Add in the descriptives for mean and median (aggregated data)

# Remove the code for line of best fit (fits a Gaussian and this is not
    # normally distributed)

# Pretty up the plots 
# Work out the means and medians for each rat (then average them)

# Add medians and means text to histogram plots 

# Make a "all functions" script and save all functions to it, run this first

# Looking through plot styles 

# 15:15 - 17:15

# Figure 2.a 
# Panel of 14, (can make 14 individual and add to word or actually panel)

# Each rat, mean photometry peak alligned to first lick within burst
# Need to change snips to allign to the first lick in a burst
    # store this as an index? Does lickcalc produce the indices of the first
    # lick of each burst? 
    # In future will also need the previous lick and the interlick interval 
        # think about how to code this 
    
    # Removing all functions and adding to "all functions" before making plots
    
# Working on figure 2
# Have the indices of the burst/runs, need the actual times (this IS in lickcalc)
    # add this as part of figure 1 for loop and call the variable later
    
# Decided not to add to the for loop, made new section of code
# Wrote new loop to make master list of first lick times for each burst
    # for each rat

# Working out how to loop around the lists of first lick times (not indices)
    # for each burst/each rat, and make blue and uv snips alligned to these events
    # (the first licks of each burst) and make the phototrials figures like 
    # with distractors 
    # All just on the last lick day for each rat (14 images for bursts and 1 
    # images for runs, 28 in total - can choose representative image) 
        # keep in mind how I will label these, knowing which iteration 
        # of the loop is which rat

# I keep repeating the load matfile in loops (not storing the 14 produced dicts.)
    # this is inefficient and needs tidying up
    # talk to JEM about it        

'''
loadmatfile 
store the blue and uv traces after loading EACH of 14 files in a similar way 
to the allBurstTimes/allBursts (will end up with 14 lists of the BLUE signal
                                readouts and 14 of the uv, might be quite data
                                heavy to store them all, but better than 
                                extracting them in place inside a loop?)

'''    

# Produced 14 plots aligned to first lick in burst
# How can I independently alter the scaling to see the peaks?
# Why do the peaks look so wildly different?
# How can I double check it is doing what I think it is?

# Means plot 
# Looking back over photometry code, how do I get the mean ALL RATS
    # (after getting the mean for EACH rat, which is done in multfig)
    
# Look at removing noise, make the trials figs (with all data on) and inspect
    # see what removing the noise does to the plots - just get rid of the 
    # initial filenames so they are never read in 
   


    
TO DO-
# Go and find which rats do not have signals (previous code, means used)
    # take the out of the analysis - remove those with no signal at all
    # then repeate the plots and choose a represntative one, and make the 
    # averaged figure using JUST THOSE WITH SIGNALS
    
# Figure out how to do the mean of all rats plot 

''' 09/03/18 '''

# Need to repeat for runs, check if signals look nicer with the first lick 
    # in the run rather than burst (longer time before no licks maybe less noise)

# 8:00 - 9:00

# Quick catch up with JEM (8:00-8:30)
# Add n trials per plot (n bursts) take from 
# Keeps reading MAT file --> pickle file ? Import dill from pickle ! 
    # stores version of file for easy access "pickles it" 
    # orderderd dictionary ?

# Adding the burst and run N text to the plots 
# Running the code for RUNS not bursts, looks nicer
# Check definition of RUN and see if possible to optimise

# 10:30 - 11:00

# Work out how to get a mean for each and plot (have done this in a very 
    # over complicated way previously, try this and then find a simpler
    # method)

# Also need to add rat number to the plots and add a YAxis label for ∆df
# delta symbol of mac = alt+j ∆

# Is there a way to get the mean value of the snips for each rat ?
    # Previously did this in excel, see if possible 
    
# Working on means fig with individual trials (each trial is a mean of ALL
    # THE RUNS of one rat, and the darker lines are means of ALL RATS)

# Need to do the same for multShadedFigure (to get an error bar like plot)


# !! THINK ABOUT HOW TO COMPARE THE PEAK FROM LICKING TO THE DISTRACTOR
    # PEAKS AND HOW CAN WE SHOW IT IS NOT JUST LICKING?
    
# Make these plots for bursts also (as we are looking at bursts not runs
    # probably during the distraction day? )

# 15:00 - 15:30

# Make mult shaded figure for bursts/runs? 
# Go through code and see if simple to plot with the variables already made 
    # for the trials fig

# Made trialsShadedFig, playing with font sizes, need to edit original function
    # to access paramters for font / label sizes 
# Making all sizing consistent and labelling axes, checking plots 

# Need to work on LONG TIME COURSE photometry plot to show licking over time 

# Not averaged, individual rat, on a lick day (choose one with decent signal)

''' 10/03/18 '''

# 19:30 - 20:00

# Quick look at x-ticks and labels for long time course plot


''' Slack message JEM
Change the axis ticks and labels. 
it's something like ax.set_yticks([0,360,720,1080]) and 
ax.set_yticklabels([0,6,12,18])

those are for made up numbers obviously. 
but then do do the sum and work out 
you have to make an array that you will feed into set_xticks 
that is based on how many samples make up each tick you want to have

so if you want one second intervals between ticks you would just 
multiply your ticks [1,2,3,4,5,6,...] by the sampling rate (fs).

if you wanted 1 minutes intervals you would multiply by fs*60, 
if you wanted 10 minutes intervals you'd multiply by fs*60*10
the only thing I'm not definite about is how our funky, 
non-ingeter fs (e.g. 1017.etc) works with all this.

'''
    
# Make tick array 

# Started with 10 min intervals between ticks 

ax7.set_xticklabels([(0*allRatFS[0]),(1*allRatFS[0]),(2*allRatFS[0]),(3*allRatFS[0]),(4*allRatFS[0])])    

ax7.set_xticks([0,(10*60*allRatFS[0]),(20*60*allRatFS[0]),(30*60*allRatFS[0]),(40*60*allRatFS[0]),(50*60*allRatFS[0]),(60*60*allRatFS[0])] )
                
Original ticks:                
1000000
2000000
3000000
4000000
       
0  mins = 0
10 mins = (10*60*allRatFS[0])
20 mins = 20*60*allRatFS[0]
30 mins = 30*60*allRatFS[0]
40 mins = 40*60*allRatFS[0]
50 mins = 50*60*allRatFS[0]
60 mins = 60*60*allRatFS[0]

# Is the UV signal scaled to the blue? or not? 

# For the long timecourse get rid of the UV signal or scale them

''' 12/03/18 '''

# 8:00 - 9:00

# Changing figure size and making long time course plot look decent
# Trying to add licks to the plot, looking over signle trial code
# Can I find the specific TTLs and the times to plot them?

# The particular plot chosen has UV and blue at similar level

# Need to use nearest event but this relies on snips aligned to 
    # an event (ie. distractor) 
    # could edit the single trial to be a longer timecourse?
    # need to fisrst make very long snips / trials (can align to distractor
    # on a lick day as this is modelled and not actual)
    # edited nearest event (normal was 10,30)
        # def nearestevents(timelock, events, preTrial=10, trialLength=600): # edited
        # works to plot the licks, but still relies on snips (aligned and 30sec)
        
    # different approach
    # just plot the TTLs of the licks on the same axis?
    # Don't have the lick TTLs stored, added line to loadmatfile
    '''
    allRatLicks = [] ...
    
    allRatLicks.append(ratdata['licks'])
    '''
# Licks added to long timecourse plot
    # Need to fix the scale and make licks clear to see
    # Choose a time course with enough zoom to see licks 
    # 10 mins? 
    # 600 seconds    
    
    # Instead of an x scale could just add in scale bar for 1min 
        # Or add ticklabels for mins
        # Add label to output (absolute light out)
        # Workout the ticks / labels correctly 
        # Double check the scale is what you think it is!!
 
TODO

# Supress output (do not need 14 * 2 individual plots, know the mean works)
# Check which lick figures are left 
# Work out what statistics will be done 
    # where the peaks will come from 
    # using just blue peaks or subracting UV 
    # where is the zero? Are they scaled or not at all? 

# Figure out how to start with NAPH1 also (no metafile here!)

# Plots so far...

# Long time course lick plot
# Averaged peaks for bursts and runs of licks 

# Next ...

# Separate bursts/runs into short and long based on top and bottom
    # 25% of burst lengths 
# Find the peaks of short runs and long runs 
# Average peak for each rat for short and long 

''' 13/03/18 '''

# 11:00

# Work on quartiles function 
# Separate the runs (as there was a peak) by high and low 
    # using upper and lower quartiles
    
# Calculate the PRE-RUN-PAUSE and plot pause against subsequent run length 

# Need to think about how to get the time of runs when 
    # to split the data into quartiles (long and short) 
    # they need to be ordered
    
# Can order to find the quartile cut offs and THEN use these
    # cut offs in a for loop to select the values that are 
    # (a) above the cut off in terms of licks in run 
    # (b) index only these (get the index boolean, logical indexing)
    
# Spent a very long time writing the following ;

'''
def quartiles(dataPoints):
 
    
    sortedPoints = sorted(dataPoints)
    mid = int(len(sortedPoints) / 2)
    
    if (len(sortedPoints) % 2 == 0):
        lowerQ = np.median(sortedPoints[:mid])
        upperQ = np.median(sortedPoints[mid:])
        
    else:
        lowerQ = np.median(sortedPoints[:mid-1])
        upperQ = np.median(sortedPoints[mid+1:])
        
    return (lowerQ, upperQ)



import math
x = 1234.5678
math.modf(x) # (0.5678000000000338, 1234.0)

def quartiles2(data):
    
    sortedPoints = sorted(data)
    nPlus1 = len(sortedPoints)+1
    X = np.median(sortedPoints)
    if (len(sortedPoints) +1) % 4 == 0 :
        print('yes')
        
        lower = (len(sortedPoints) + 1) * 0.25
        upper = (len(sortedPoints) + 1) * 0.75
        print(lower)
        print(upper)
        
    else:
        
        decimal, integer = math.modf(len(sortedPoints)+1)

        lower = integer*(nPlus1*0.25)+ ((integer*(nPlus1 * 0.25) + 1) * (decimal*(nPlus1 * 0.25)))
        upper = integer*(nPlus1*0.75)+ ((integer*(nPlus1 * 0.75) + 1) * (decimal*(nPlus1 * 0.75)))
        print(lower)
        print(upper)
        
'''

# Discovered build in, np.percentile(a,25) and np.percentil(a,75)

# Work out how to subset data, want to splice the list from the 25th and 75th percentiles
    # But don't want to keep them ordered 
    # Use logical indexing to access the indices in all lists with the same dims
    
    # Add a col of T/F 1/0 and use booleans to select the lick start times to 
        # include 
    
    # Think about how it links in to the snips, define the start of the snip 
         # by the time of the short runs and then the long runs only 
         
# Can work on finding the pause before the burst 
     # Comparing the short pauses, long pauses, short runs and long runs 
     
     
''' 15/03/18 '''
# 13:00 - 14:40

# Working on the pre-run / bre-burst pause 
# That pause must be at least 10 seconds as defined this previously in the run
    # calculator 

# Find the long and short bursts - done with quartiles
# Separate the rats by their long and short bursts (done)

# Find the indices of the burst first lick - go back to lick calc and check if
    # it produces the lick index for the burst/run first lick 


'''UNSURE IF THE RUN INDICES ARE CORRECT, THOUGHT RUNS WERE NOTHING FOR 10 SECONDS'''

'''
preRunPauses = []  
allPreRunPauses = []  
for runIndexIndex, runIndexList in enumerate(allRunIndices):
    tempLickList = allRatLicks[runIndexIndex] # accesses 1, to 14 indices for the lists
    # check this, seems to have index 1 as always a run, the first run
    for runIndex in runIndexList:
        preRunPause = tempLickList[runIndex] - tempLickList[runIndex-1]
        preRunPauses.append(preRunPause)
        
    allPreRunPauses.append(preRunPauses)

'''


# Do I already have the ILIs? rILI variable looks like the interval between the 
    # first lick in the run and the preceeding lick (should all be over 10 seconds 
    # as this was the definition in LickCalc)

'''
# Figure 10 - Finding the pauses before run (preRunPauses) and how this relates
# to burst length 
# regression? As both continuous??? 

# Linear regression --> see R notes 

'''

# Run a linear regression 
scipy.stats.linregress

# Ran regression 
r-squared: 0.0252415143382
p_value
Out[455]: 0.00573622449834571
slope
Out[456]: 0.13265944745570354
r_value
Out[457]: 0.15887578273045813

''' Interpretation '''
# http://blog.minitab.com/blog/adventures-in-statistics-2/how-to-interpret-a-regression-model-with-low-r-squared-and-low-p-values

# Looks like there is incredibly weak relationship OR linear model doesn't fit data well

# Repeat all of this for the bursts (although the neural data shows no peak) would 
    # be useful to look at behaviour for both bursts and runs 

# THEN, last bit for lick figures
    # look at peaks alligned to LONG bursts and SHORT bursts 
    # figure out how to get the snips around these time points (check they are times)
    # as events  

++++++++++++++++++++++++++ BREAK

# 15:00 - 17:00


   # 426 - 455 Linear regressions, runs is significant but incredibly weak (2%)
   # bursts is even lower and not significant 
   # looks like relationship is NOT linear, burst length is not well predicted by 
   # the pause before the burst or pause before the run 

# Last licking figure

    # Make photometry figures alligned to short (lower quartile) and long (upper quartile) 
    # Run lengths (can do for bursts but very little evidence of peak as grouped)


# Finding times for short and long bursts using quartiles 

'''
lowerqRunTimes = []
uppqRunTimes = []
mid50RunTimes = []

# Might need the index and the value for both lists ??
for i, listofindices in enumerate(allLogIndRuns):
    
    for j, runIndex in enumerate(listofindices):
        
        #print(i,j) i is the list index and j is the item index
        
        if runIndex == 'LOWER':
            lowrun = allRunsTimes[i][j]
            lowerqRunTimes.append(lowrun)
           
        if runIndex == 'UPPER':
            upprun = allRunsTimes[i][j]
            uppqRunTimes.append(upprun)
#                
        if runIndex == 'MIDDLE':
            midrun = allRunsTimes[i][j]
            mid50RunTimes.append(midrun)
            
'''

# Need to do something to the for loops

# Thought I'd fixed it but haven't!! Have now got 14 lists of 75 values 
    # need to move around the appends in the loop and figure out when to add lists
    # of values 
    # Forgot to re-initialise the temp list to [] empty after the loops


•••••••••••••••••••••••••••••••••• BREAK

# 17:20 - 18:15

# Making photometry figures alligned to short and long runs (first lick in these)

# Making 14 individual plots and also the averaged plots 

    # Make sure to remove the rat with 0 short bursts from the mean plot  
    # And the same with long bursts 

# Kept zero's in and didn't affect average much so left them there
# Made plots for short runs and long runs

# Made combined plot for short and long JUST BLUE SIGNALS - could use 2 shades of blue
    # or totally different colours     
    
 # Fill in the comments at top of script (to exaplin what plots it makes at the moment)

# Move onto distraction figures ... 


''' 16/03/18 '''

# 8:00 

# Distractionn figures  (file = Distraction_photometry_figures)
# Behavioural figs. in THPH1 and 2 behaviour

# Bar scatter plots done, add them to individual script
# Get behavioural figures too, cumulative licking on distraction day vs lick day 

# Move the plotting functions and code to new folder to produce all behavioural 
    # and photometry figures for distraction 
    
# Remaking barscatter plots for percentage distracted, adding axes labels
# Finding data for photometry peak (delta df) on lick day and distraction day
    # In respons to DISTRACTORS and modelled distractors (defined as 2 seconds following
     #                                                     onset)
    

# Finding data - peaks for distractED and NOTdistractED


# There is no for loop in the distraction data set 

# Previously I had MANUALLY taken out the data to make the means file 
# Add in the for loop and get all the data in Python NOT excel  - will do this later

# Found the peaks!!
'''

lick	-0.001217125	0.000859069	-0.001190911	0.036421799	0.008933065	-0.002367187	0.026656246	0.008760555	0.000819196	0.003400855	0.012282488	0.008551392	0.034570625	0.040277452
dis	0.002176149	0.000233842	0.058384302	0.03030952	0.004967007	-0.002709698	0.04434895	0.008963946	0.017853078	0.036290338	0.035266618	0.041162435	0.040683707	0.051224802
distracted	0.003363358	0.000194394	0.060783732	0.020370505	0.01726766	-0.003759903	0.041509866	0.012103415	0.019385049	0.036805379	0.042935575	0.050501034	0.074754689	0.042745122
notdist	0.001005643	-0.000233414	0.047120378	0.039605352	0.005720193	-0.002479069	0.055897022	0.009787216	0.01537006	0.036403637	0.024719976	0.026275861	0.0384651	0.067704732

'''

# Making barscatter using the peaks (2 seconds peaks)

# Altering barscatter function to add titles
# Added title='none' parameter :

if title != 'none':
        plt.title(title, fontsize=14)
        
# Finding a good example for single trial figure 
# Good --> 

datafile = datafolder + 'thph2.5distraction.mat'
trial = 5


datafile = datafolder + 'thph2.3distraction.mat'
trial = 8
trial = 17 # very good
# Getting rid of spines 


 ''' 17/03/18 '''
 
 # 10:00 - 17:00
 
 # Working on distraciton raster for distraction day 
 
 # At the moment code is very specific to the individual rat 
     # Corrected for this rat having the last lick as a distractors etc.
     # Specifying the cut off for colour change by N distractions (40/65) so
       # 26 not distracted cut off manual here: 
           
         for ith, trial in enumerate(rasterData):
        if ith < 26:
 
            ax.vlines(trial, ith + .5, ith + 1.5)
        else:
            ax.vlines(trial, ith + .5, ith + 1.5, color='blue')
        
# Play around with axes and scale bars, 

# Try to use scatter plots rather than V.LINEs and see if it looks better 

            
    for ith, trial in enumerate(rasterData): 
        xvals = [x for x in trial]
        yvals = [ith+0.5] * len(xvals) 
        ax.scatter(xvals, yvals, marker='|', color='k')
        
# Issues of overlap! Changing the yvals doesnt seem to fix the overlap issue
# Temporary fix with different marker style ('.' not vline)

# Remove axes and add time scale bar

# Repeat for that rat on licking day 
    # This particular rat has 40 trials out of 65 distracted 
    
# Making and saving figures 

#     fig.savefig('/Volumes/KPMSB352/PHOTOMETRY MMIN18/PDF figures/FILENAME.pdf')        
    

# Size 4,5 (barscatter)



  
# 17:10 - 19:00

# Find where the peak data are defined, and work out how to get these for different 
    # time points 
    
# Want peaks or averaged activity across the preceding 2 seconds 
# Averaged activity in the whole 5 or 10 seconds after (maybe between 2 seconds and 10)

# Making barscatter for 2 seconds before and 20 seconds after averaged activity 

# Looking at broken axis example (would make plot look better to save the outliers ruining it)

# Axis 1 -> 0.025 - -0.025
# Axis 2 -> 0.03 - 0.04
# Axis 3 --> -0.03 - -0.04
   
# 19:00 - 19:50 

# Making and saving scatterbar plots for 2 seconds before and 20 seconds after distract(tion)/not
# Fixing issue with marker edge color
    # Jaime sent link to styles setting (was overridding)
    
    ''' https://matplotlib.org/users/customizing.html ''' 
 
    
''' 10/04/18 '''

# Need to go through all files again and catch up 
# What has been done, what needs doing 

# Make a clear pipeline from start to finish for 

(1) Behavioural analysis and paper
(2) Phototmetry analysis and paper 

Work on gettng the lick ttls onto the existing plots too 
    
''' 16/04/18 ''' 

#
#
#
#
    
==============================




    # T-test comparisons, (1) 3 lick bursts non distracted and distracted days (-1 and 0)
# Matrix maker as function 
# Continue modularising code
# Distractor analysis, calculate if distracted or not and then compare with med
    # See how often there is a 4th lick 
    # Look at post distraction pause (ILI)
# Start DPCP script 
# Look over MATLAB converter and see what will need doing for THPH analysis 

# What files does Python need from synapse?
    # What codes do each TTL mean
    # Which streams do we need 
    # How are the streams indexed?
    


#? Heat maps of post distraction pauseS? Can not do this for DIS1 and just onset 

# As an aside from DIS1 --> look up THPHT1 matlab conversion script and see 
    # what needs to be done


# Think about classification algorithms, can machine learning predict if distracted
#or not based on licking OR based on brain photometry signals??? this would be cool 


            