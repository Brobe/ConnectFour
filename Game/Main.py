import GUI
from Player import *
import GameEnd

players = []
w = 7 #width of the playfield
h = 6 #height of the playfield


def round(player, field):
    incol = int(input("Player " + player.name + "s (" + player.marker + ")turn!\nWhere would you want to place your brick? (choose a value between 1 and " + str(w) + "\n")) - 1
    for row in field[::-1]:
        if(row[incol] == 0):
            row[incol] = player.marker
            break
    return field


def run():
    playField = [[0 for col in range(w)] for row in range(h)]
    GUI.printField(playField)


    inplayers = input("How many players will be playing?\n")
    for index in range(0,int(inplayers)):
        playername = input("Name of player #"+str(index+1)+"?\n")
        playermarker = input("What marker does "+str(playername)+" want?\n")
        player = Player(playername,playermarker)
        players.append(player)

    playerturn = 0
    while(True):
        if(playerturn == len(players)):
            playerturn = 0

        playField = round(players[playerturn], playField)
        GUI.printField(playField)
        if(GameEnd.gameover(players[playerturn], playField)):
            break
        playerturn+=1

    print("Player " + players[playerturn].name + " wins!")
    return








### Starting the game!
run()