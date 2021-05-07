# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 09:41:42 2021

@author: Robbie
"""
import matplotlib.pyplot as plt
def CreatePitch(): 
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_facecolor('xkcd:green')
    
    # Pitch outline
    plt.plot([0, 0], [-20, 90], color='white')
    plt.plot([0, 40], [90, 90], color='white')
    plt.plot([40, 40], [-20, 90], color='white')
    plt.plot([0, 40], [-20, -20], color='white')
    plt.plot([0, 40], [0, 0], color='white')
    plt.plot([0, 40], [70, 70], color='white')
    
    # Infield brick marks
    plt.plot([19, 21], [19, 21], color='white')
    plt.plot([19, 21], [21, 19], color='white')
    plt.plot([19, 21], [49, 51], color='white')
    plt.plot([19, 21], [51, 49], color='white')
    
    # End zone brick marks
    plt.plot([19, 21], [-9, -11], color='white')
    plt.plot([19, 21], [-11, -9], color='white')
    plt.plot([19, 21], [79, 81], color='white')
    plt.plot([19, 21], [81, 79], color='white')
    
    
    # Print pitch
    plt.axis('scaled')
    #plt.show()
