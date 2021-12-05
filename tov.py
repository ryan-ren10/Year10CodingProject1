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

def getTOV(data, dic, player):
    tov = 0
    seasons = 0
    for i in range(0, len(data)):
        to = float(data[i][dic['TOV']]) 
        fta = float(data[i][dic['FTA']])
        fga = float(data[i][dic['FGA']]) 
        tovVal = 100*to/(fga + 0.44*fta + to)
        if (player == 'all') or (player == data[i][dic['Player']]):
            tov += tovVal 
            seasons += 1
    tovAv = round(tov/seasons, 2) 
    return tovAv 
getTOV(playerPerGame, playerPerGameCol, 'Kobe Bryant')
getTOV(playerPerGame, playerPerGameCol, 'Lebron James')
getTOV(playerPerGame, playerPerGameCol, 'Michael Jordan') 
getTOV(lgPerGame, lgPerGameCol, 'all') 

def pieTOV():
    #TS Values 
    lbj = getTOV(playerPerGame, playerPerGameCol, 'Lebron James')
    mj = getTOV(playerPerGame, playerPerGameCol, 'Michael Jordan') 
    kobe = getTOV(playerPerGame, playerPerGameCol, 'Kobe Bryant')
    lg = getTOV(lgPerGame, lgPerGameCol, 'all')

    explode = (0, 0.1, 0, 0)
    names = ["Lebron", "MJ", "Kobe", "NBA"] 
    sizes = [lbj, mj, kobe, lg]
    labels = []
    sumAll = lbj + mj + kobe + lg

    for n in range(0,len(sizes)):
        decimal = sizes[n]/sumAll
        piePercent = "{:.2%}".format(decimal)
        labels.append( names[n] + " (" + piePercent + ")\nTOV: " + str(sizes[n]) + '%' )  
     
    fig1, wedges = plt.subplots()
    plt.title('Average Player TOV%') 
    plt.gca().axis("equal")
    wedges, texts= plt.pie(sizes, explode=explode, startangle=90, labels=labels,
                            wedgeprops = { 'linewidth': 2, "edgecolor" :"k","fill":False,  } ) 

    #Image pie chart positions
    positions = [(-0.4,0.5),(-0.47,-0.5),(0.5,-0.45), (0.4, 0.422)]
    zooms = [0.6,0.4,0.2, 0.2]

    for i in range(4):
        fn = "{}.png".format(names[i].lower())
        lib.imgToPie(fn, wedges[i], xy=positions[i], zoom=zooms[i])
        wedges[i].set_zorder(10) 

    plt.show()
    return



