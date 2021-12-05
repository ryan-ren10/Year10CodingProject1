import library as lib 
import bpm as box 
import tov as to 
import assists_ows_steals as aos 
import fg_percent as trueShoot 

while True:
    print('\nStats to choose from:\n-ASSISTS\n-OWS\n-STEALS\n-TOV\n-TS%\n-BPM\n\nTo quit, type in "quit".\n ') 
    x = input('Choose a stat: ')
    if x.upper() == 'ASSISTS':
        aos.assistPie()
    elif x.upper() == 'STEALS':
        aos.stealPie()
    elif x.upper() == 'OWS':
        aos.owsPie() 
    elif x.upper() == 'TOV':
        to.pieTOV() 
    elif x.upper() == 'BPM':
        box.barBPM()
    elif x.upper() == 'TS%':
        trueShoot.pieTS()
    elif x.upper() == 'QUIT':
        break 
    else:
        print('Please type one of the stats indicated above.') 



