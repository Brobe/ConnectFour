def printField(matrix, ):
    for row in matrix[0:]:
        line = '| '
        for char in row[0:]:
            line += str(char) + ' | '
        print(line)
