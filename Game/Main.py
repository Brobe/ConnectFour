import GUI
from Player import *
import GameEnd

players = []

def round(player, field, file):
    incol = int(input("Player " + player.name + "s (" + player.marker + ") turn!"
                                                                        "\nWhere would you want to place your brick? (choose a value between 1 and " + str(len(field)) + ")\n")) - 1
    if(incol > len(field)):
        print("That value can not be chosen.")
        return round(player, field)
    if(field[0][incol] != 0):
        print("Already chosen, try again")
        return round(player, field)
    for row in field[::-1]:
        if(row[incol] == 0):
            row[incol] = player.marker
            file.write("Player " + str(player.name) + " chose " + str(incol+1) + "\n")
            break
    return field


def run():
    logfile = open("log.txt", "a")
    highfile = open("highscore.txt", "r")
    highscorelist = highfile.readlines()
    highfile.close()
    highscoretimes = 0
    highscorename = ''

    winners = {}
    for w in highscorelist:
        w = w.rstrip("\n")
        if w in winners:
            winners[w] += 1
        else:
            winners[w] = 1

    for winner,times in winners.items():
        if(times > highscoretimes):
            highscoretimes = times
            highscorename = winner

    print("Player "+highscorename+" has won "+str(highscoretimes)+" times!")


    infield = input("How big do you want the playfield (for example 7x6)\n")
    w = int(infield.split('x')[0]) #width of the playfield
    h = int(infield.split('x')[1]) #height of the playfield
    totalmoves = w*h
    movesdone = 0
    playField = [[0 for col in range(w)] for row in range(h)]
    inplayers = input("How many players will be playing?\n")
    for index in range(0,int(inplayers)):
        playername = input("Name of player #"+str(index+1)+"?\n")
        playermarker = input("What marker does "+str(playername)+" want?\n")
        if(playermarker == '0'):
            print("You can not chose that marker")
            return run()
        player = Player(playername,playermarker)
        players.append(player)
    GUI.printField(playField)

    playerturn = 0
    while(True):
        if(playerturn == len(players)):
            playerturn = 0

        playField = round(players[playerturn], playField, logfile)
        movesdone += 1
        GUI.printField(playField)
        if(GameEnd.gameover(players[playerturn], playField)):
            break
        if (movesdone > totalmoves-1):
            incon = input("No moves left, do you want to play again? (Y/N)")
            if(incon == "y"):
                run()
            else:
                return
        playerturn+=1

    winningplayer = players[playerturn]
    print("Player " + winningplayer.name + " wins!")
    logfile.write("Player " + winningplayer.name + " wins!\n")
    logfile.close()
    highsfile = open("highscore.txt", "a")
    highsfile.write(winningplayer.name + "\n")
    return








### Starting the game!
run()