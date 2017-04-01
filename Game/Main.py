import GUI
from Player import *

players = []

def gameover():
    return True

def getWinner():
    return players[0]

def run():
    w = 7 #width of the playfield
    h = 6 #height of the playfield
    playField = [[0 for col in range(w)] for row in range(h)]
    GUI.printField(playField)

    inplayers = input("How many players will be playing?\n")
    for index in range(0,int(inplayers)):
        playername = input("Name of player #"+str(index)+"?\n")
        playermarker = input("What marker does "+str(playername)+" want?\n")
        player = Player(playername,playermarker)
        players.append(player)

    playerturn = 0
    while(True):
        if(playerturn == len(players)):
            playerturn = 0

        if(gameover()):
            break
        playerturn+=1

    print("Player " + getWinner().name + " wins!")

    #incol = input("Where would you want to place your brick? (choose a value between 1 and " + str(w) + "\n")







    return








### Starting the game!
run()