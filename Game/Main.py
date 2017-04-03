import GUI
from Player import *
import GameEnd

players = [] #All players in this list will be in the game

# Method for one round of the game. It will check if the colum has been filled or if the input is not correct.
#when the round is almost complete it writes to the logfile.
def round(player, field, file):
    incol = int(raw_input("Player " + player.name + "s (" + player.marker + ") turn!\nWhere would you want to place your brick? (choose a value between 1 and " + str(len(field)) + ")\n")) - 1

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

#The whole game is runned from this method.
def run():
    logfile = open("log.txt", "a") #File that stores the audit.
    highfile = open("highscore.txt", "r") #File that stores the winners.
    highscorelist = highfile.readlines()
    highfile.close()
    highscoretimes = 0
    highscorename = ''

    winners = {} #Dictionary for all the winners
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

    infield = raw_input("How big do you want the playfield (for example 7x6)\n")
    w = int(infield.split('x')[0]) #width of the playfield
    h = int(infield.split('x')[1]) #height of the playfield

    #totalmoves and movesdone keeps track when the game is out of moves.
    totalmoves = w*h
    movesdone = 0

    playField = [[0 for col in range(w)] for row in range(h)]
    inplayers = raw_input("How many players will be playing?\n")

    #Getting the name and what marker the player want and then creating the players.
    for index in range(0,int(inplayers)):
        playername = raw_input("Name of player #"+str(index+1)+"?\n")
        playermarker = raw_input("What marker does "+str(playername)+" want?\n")
        if(playermarker == '0'):
            print("You can not chose that marker")
            return run()
        player = Player(playername,playermarker)
        players.append(player)

    GUI.printField(playField) #Printing the playfield
    playerturn = 0

    while(True): #Running the game.
        #Running through the list of players.
        if(playerturn == len(players)):
            playerturn = 0

        playField = round(players[playerturn], playField, logfile)
        movesdone += 1
        GUI.printField(playField) #Printing the playfield

        #Checking if the game should end.
        if(GameEnd.gameover(players[playerturn], playField)):
            break
        if (movesdone > totalmoves-1):
            incon = raw_input("No moves left, do you want to play again? (Y/N)")
            if(incon == "y"):
                run()
            else:
                return
        playerturn+=1

    #Printing out the winning player, writing to the logfile who won and then saving the winner to the highscore file.
    winningplayer = players[playerturn]
    print("Player " + winningplayer.name + " wins!")
    logfile.write("Player " + winningplayer.name + " wins!\n")
    logfile.close()
    highsfile = open("highscore.txt", "a")
    highsfile.write(winningplayer.name + "\n")
    return


### Starting the game!
run()