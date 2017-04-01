import GUI
import Player

def run():
    w = 7 #width of the playfield
    h = 6 #height of the playfield
    playField = [[0 for col in range(w)] for row in range(h)]
    GUI.printField(playField)
    winner = False

    players = []
    inplayers = input("How many players will be playing?")
    for index in range(0,inplayers):
        playername = input("Name of player #"+str(index)+"?\n")
        playermarker = input("What marker does "+str(playername)+" want?\n")
        players.append(Player(playername,playermarker))

    while(winner == False):

    #incol = input("Where would you want to place your brick? (choose a value between 1 and " + str(w) + "\n")







    return








### Starting the game!
run()