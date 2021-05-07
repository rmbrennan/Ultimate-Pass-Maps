# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:42:07 2021

@author: Robbie
"""
import os
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/Robbie/Documents/Frisbee Stuff/WSP Pass Maps")

# Import existing functions
import get_sheet_data
import CreatePitch

# Download google sheet data
df = get_sheet_data.get_sheet_data()

# Create (X, Y) coordinates for passes and filter dataset
df['Start_X'] = df.groupby(['Possession'])['Disc_X'].shift(1)
df['Start_Y'] = df.groupby(['Possession'])['Disc_Y'].shift(1)

df = df.dropna(axis = 0)
df = df.reset_index(drop = True)

# Calculate pass distance
df['Dist'] = np.sqrt((df['Start_X'] - df['Disc_X'])**2 + (df['Start_Y'] - df['Disc_Y'])**2)

#%%
# Simple test to map all passes (completions and goals different colours)
CreatePitch.CreatePitch()

for x in range(len(df['Disc_X'])):
    if df['Result'][x]=='COMPLETED':
        plt.plot((df['Start_X'][x], df['Disc_X'][x]), (df['Start_Y'][x], df['Disc_Y'][x]), color = 'red')
    if df['Result'][x]=='GOAL':
        plt.plot((df['Start_X'][x], df['Disc_X'][x]), (df['Start_Y'][x], df['Disc_Y'][x]), color = 'black')
        
plt.show()

#%%
import dash
