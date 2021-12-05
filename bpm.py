import library as lib
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import pandas as pd
import numpy as np
import csv

#Player Data
playerPerGame = lib.loadList('per_game_stats.csv') 
playerPerGameCol = {'FG':8, 'FGA':9, 'FG%':10, '3P':11, '3PA':12, '3P%':13,'FT':18, 'FTA':19, 'TRB':23, 'AST':24, 'STL':25, 
                    'BLK': 26, 'TOV':27, 'PTS':29, 'Player':30}

playerAdv = lib.loadList('advanced_stats.csv') 
playerAdvCol = {'OWS':19, 'BPM':25, 'Player': 27} 

#League Data
lgPerGame = lib.loadList('lg_per_game.csv') 
lgPerGameCol = {'Player':0, 'FG':7, 'FGA':8, 'FT':17, 'FTA': 18, 'TRB':22, 'AST':23, 'STL':24, 'BLK':25, 'TOV':26, 'PTS': 28} 

lgAdvanced = lib.loadList('lg_advanced.csv')  
lgAdvancedCol = {'Player':0, 'OWS':18, 'BPM':24} 

def getBPM(data, dic, player):
    seasons = 0
    bpm = 0 
    for i in range(0, len(data)):
        bpmVal = float(data[i][dic['BPM']])
        if (player == 'all') or (player == data[i][dic['Player']]):
            bpm += bpmVal
            seasons += 1 
    avBPM = round(bpm/seasons, 1) 
    return avBPM 

def barBPM():

    kobe = getBPM(playerAdv, playerAdvCol, 'Kobe Bryant')
    mj = getBPM(playerAdv, playerAdvCol, 'Michael Jordan')
    lebron = getBPM(playerAdv, playerAdvCol, 'Lebron James')
    lg = getBPM(lgAdvanced, lgAdvancedCol, 'all') 

    data = [lg, kobe, mj, lebron] 

    fig, ax = plt.subplots()

    xPos = np.arange(len(data))

   
    labels=['NBA', 'Kobe', 'MJ', 'Lebron']
    colors = ['blue', 'purple', 'red', 'orange']   
    ax.bar(xPos, data, color=colors)
    ax.set_ylabel('Box Plus/Minus')
    plt.xticks(xPos, labels)
    
    #For each bar plot values
    for x, y in zip(xPos, data):
        label = y
        plt.annotate(label,(x,y), textcoords='offset points', xytext=(0,-10), ha='center')
    #Plot images for each bar 
    for i, (label, value) in enumerate(zip(xPos, data)):
        img = plt.imread("{}.jpg".format(labels[i].lower()))
        if (i == 0) or (i == 1):
            plt.imshow(img, extent=[label-0.3, label+0.3, value-2.9, value-0.8], aspect='auto', zorder=2)
        else:
            plt.imshow(img, extent=[label-0.3, label+0.3, value/2-1.1, value/2+1], aspect='auto', zorder=2)

        plt.xlim(-0.5, 3.7)
        plt.ylim(-5, 11)


    plt.axhline(y=0, color='grey', linewidth=2) 
    plt.axhline(y=lg, color='magenta', linestyle='dashed', label='League Average', linewidth=3)
    plt.title('Average Player and League Box +/-')
    ax.legend()  

    plt.show()  
    return 





