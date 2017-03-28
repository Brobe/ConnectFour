def printField(matrix):
    for x in matrix[0:]:
        line = '| '
        for y in x[0:]:
            line += str(y) + ' | '
        print(line)
