def gameover(player, field):
    w = len(field[0])
    h = len(field)

    #Vertical check
    inARow = 0
    for colindex in range(w):
        for row in field:
            if(inARow == 4):
                return True
            if(row[colindex] == player.marker):
                inARow += 1
                if (inARow == 4):
                    return True
            else:
                inARow = 0

    #Horizontal check
    inARow = 0
    for row in field:
        for colindex in row:
            if(inARow == 4):
                return True
            if (colindex == player.marker):
                inARow += 1
                if (inARow == 4):
                    return True
            else:
                inARow = 0

    #Diagonal falling,
    #1. colum iteration
    for colindex in range(1,w-4):
        inARow = 0
        for index in range(h-(colindex-1)):
            if (inARow == 4):
                return True
            if(field[index][colindex+index] == player.marker):
                inARow += 1
                if(inARow == 4):
                    return True
            else:
                inARow = 0
    #2. row iteration
    for rowindex in range (1,h-3):
        inARow = 0
        for index in range(h-rowindex):
            if(inARow == 4):
                return True
            if(field[rowindex+index][index] == player.marker):
                inARow += 1
                if(inARow == 4):
                    return True
            else:
                inARow = 0
    #3. for row and colum having the same value
    inARow = 0
    for index in range(h):
        if (inARow == 4):
            return True
        if (field[index][index] == player.marker):
            inARow += 1
            if (inARow == 4):
                return True
        else:
            inARow = 0


    #Diagonal rising
    #1. colum iteration
    inARow = 0
    for index in range(0, w-4):
        for colindex in range(1, w-index):
            if(inARow == 4):
                return True
            if(field[h-colindex][colindex+index] == player.marker):
                inARow += 1
                if(inARow == 4):
                    return True
            else:
                inARow = 0
    #2. row iteration
    inARow = 0
    for index in range(3,h-1):
        for rowindex in range(0,index+1):
            if (inARow == 4):
                return True
            if (field[index-rowindex][rowindex] == player.marker):
                inARow += 1
                if (inARow == 4):
                    return True
            else:
                inARow = 0
    #3. for [n][n] being the same value
    inARow = 0
    for index in range(h):
        if (inARow == 4):
            return True
        if (field[(h-1)-index][index] == player.marker):
            inARow += 1
            if (inARow == 4):
                return True
        else:
            inARow = 0
    return False
