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

#TS Function
def TS(data, dic, player):
    ts = 0
    seasons = 0
    for i in range(0, len(data)):
        pts = float(data[i][dic['PTS']])    
        fga = float(data[i][dic['FGA']])
        fta = float(data[i][dic['FTA']])
        tsVal = pts/(2.0*(fga + 0.44*fta))
        if (player == 'all') or (player == data[i][dic['Player']]):
            ts += tsVal
            seasons += 1
    avTS = round(ts/seasons, 3) 
    return avTS 



def pieTS():
    #TS Values 
    lbj = TS(playerPerGame, playerPerGameCol, 'Lebron James')
    mj = TS(playerPerGame, playerPerGameCol, 'Michael Jordan') 
    kobe = TS(playerPerGame, playerPerGameCol, 'Kobe Bryant')
    lg = TS(lgPerGame, lgPerGameCol, 'all')

    explode = (0.1, 0, 0, 0) 
    names = ["Lebron", "MJ", "Kobe", "NBA"] 
    sizes = [lbj, mj, kobe, lg]
    labels = []
    sumAll = lbj + mj + kobe + lg

    for n in range(0,len(sizes)):
        decimal = sizes[n]/sumAll
        piePercent = "{:.2%}".format(decimal)
        tsPercent= "{:.1%}".format(sizes[n])
        labels.append( names[n] + " (" + piePercent + ")\nTS: " + tsPercent )  
     
    fig1, wedges = plt.subplots()
    plt.title('True Shooting %')
    plt.gca().axis("equal")
    wedges, texts= plt.pie(sizes, explode=explode, startangle=90, labels=labels,
                            wedgeprops = { 'linewidth': 2, "edgecolor" :"k","fill":False,  } ) 

    #Image pie chart positions
    positions = [(-0.4,0.5),(0,-0.5),(0.5,-0.35), (0.3, 0.45)]
    zooms = [0.4,0.4,0.2, 0.2]

    for i in range(4):
        fn = "{}.png".format(names[i].lower())
        lib.imgToPie(fn, wedges[i], xy=positions[i], zoom=zooms[i])
        wedges[i].set_zorder(10) 

    plt.show()
    return  





