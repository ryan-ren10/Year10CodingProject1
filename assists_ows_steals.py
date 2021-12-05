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
#<------------------------------------ Start of getVal Function ------------------------------->#
def getVal(data, dic, player, stat):
    statVal = 0
    seasons = 0
    for i in range(0, len(data)):
        if (player == 'all') or (player == data[i][dic['Player']]):
            statVal += float(data[i][dic[stat]]) 
            seasons += 1
       
    statAv = round(statVal/seasons, 1) 
    return statAv 
#<------------------------------------ End of getVal Function ------------------------------->#

#<------------------------------------ Start of Assist Pie Chart ------------------------------->#
def assistPie():
    lbj = getVal(playerPerGame, playerPerGameCol, 'Lebron James', 'AST')
    mj = getVal(playerPerGame, playerPerGameCol, 'Michael Jordan', 'AST') 
    kobe = getVal(playerPerGame, playerPerGameCol, 'Kobe Bryant', 'AST')
    lg = getVal(lgPerGame, lgPerGameCol, 'all', 'AST') 

    explode = (0.1, 0, 0, 0) 
    names = ["Lebron", "MJ", "Kobe", "NBA"] 
    sizes = [lbj, mj, kobe, lg]
    labels = []
    sumAll = lbj + mj + kobe + lg 

    for n in range(0,len(sizes)):
        decimal = sizes[n]/sumAll
        piePercent = "{:.2%}".format(decimal) 
        labels.append( names[n] + " (" + piePercent + ")\nAPG: " + str(sizes[n]) )

    fig1, wedges = plt.subplots()
    plt.title('Average Assists Per Game') 
    plt.gca().axis("equal")
    wedges, texts= plt.pie(sizes, explode=explode, startangle=90, labels=labels,
                            wedgeprops = { 'linewidth': 2, "edgecolor" :"k","fill":False,  } )

    #Image pie chart positions
    positions = [(-0.5,0.4),(0,-0.5),(0.9,0.1), (0.2, 0.55)]
    zooms = [0.6,0.4,0.25, 0.2]

    for i in range(4):
        fn = "{}.png".format(names[i].lower())
        lib.imgToPie(fn, wedges[i], xy=positions[i], zoom=zooms[i])
        wedges[i].set_zorder(10)  
    
    plt.show()
    return


#<------------------------------------ End of Assist Pie Chart ------------------------------->#

#<------------------------------------ Start of OWS Pie Chart -------------------------------># 

def owsPie():
    lbj = getVal(playerAdv, playerAdvCol, 'Lebron James', 'OWS')
    mj = getVal(playerAdv, playerAdvCol, 'Michael Jordan', 'OWS') 
    kobe = getVal(playerAdv, playerAdvCol, 'Kobe Bryant', 'OWS')
    lg = getVal(lgAdvanced, lgAdvancedCol, 'all', 'OWS') 

    explode = (0.1, 0, 0, 0) 
    names = ["Lebron", "MJ", "Kobe", "NBA"] 
    sizes = [lbj, mj, kobe, lg]
    labels = []
    sumAll = lbj + mj + kobe + lg 

    for n in range(0,len(sizes)):
        decimal = sizes[n]/sumAll
        piePercent = "{:.2%}".format(decimal) 
        labels.append( names[n] + " (" + piePercent + ")\nOWS: " + str(sizes[n]) )

    fig1, wedges = plt.subplots()
    plt.title('Average Offensive Win Share') 
    plt.gca().axis("equal")
    wedges, texts= plt.pie(sizes, explode=explode, startangle=90, labels=labels,
                            wedgeprops = { 'linewidth': 2, "edgecolor" :"k","fill":False,  } )

    #Image pie chart positions
    positions = [(-0.5,0.4),(0,-0.5),(1,0.3), (0.2, 0.55)]
    zooms = [0.6,0.4,0.25, 0.2]

    for i in range(4):
        fn = "{}.png".format(names[i].lower())
        lib.imgToPie(fn, wedges[i], xy=positions[i], zoom=zooms[i])
        wedges[i].set_zorder(10)  
    
    plt.show()
    return



#<------------------------------------ End of OWS Pie Chart ------------------------------->#


#<------------------------------------ Start of Steals Pie Chart ------------------------------->#

def stealPie():
    lbj = getVal(playerPerGame, playerPerGameCol, 'Lebron James', 'STL')
    mj = getVal(playerPerGame, playerPerGameCol, 'Michael Jordan', 'STL') 
    kobe = getVal(playerPerGame, playerPerGameCol, 'Kobe Bryant', 'STL')
    lg = getVal(lgPerGame, lgPerGameCol, 'all', 'STL') 

    explode = (0, 0.1, 0, 0) 
    names = ["Lebron", "MJ", "Kobe", "NBA"] 
    sizes = [lbj, mj, kobe, lg]
    labels = []
    sumAll = lbj + mj + kobe + lg 

    for n in range(0,len(sizes)):
        decimal = sizes[n]/sumAll
        piePercent = "{:.2%}".format(decimal) 
        labels.append( names[n] + " (" + piePercent + ")\nSPG: " + str(sizes[n]) )

    fig1, wedges = plt.subplots()
    plt.title('Average Steals Per Game') 
    plt.gca().axis("equal")
    wedges, texts= plt.pie(sizes, explode=explode, startangle=90, labels=labels,
                            wedgeprops = { 'linewidth': 2, "edgecolor" :"k","fill":False,  } )

    #Image pie chart positions
    positions = [(-0.5,0.4),(0,-0.5),(0.9,0.1), (0.2, 0.55)]
    zooms = [0.6,0.4,0.25, 0.2]

    for i in range(4):
        fn = "{}.png".format(names[i].lower())
        lib.imgToPie(fn, wedges[i], xy=positions[i], zoom=zooms[i])
        wedges[i].set_zorder(10)  
    
    plt.show()
    return



#<------------------------------------ End of Steals Pie Chart ------------------------------->#