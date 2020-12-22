
# https://adventofcode.com/2020/day/5#part2 


def findRow(file):
    listOfRows = [x for x in range(0, 128)]

    for i in range(0, 7):
        if file[i] == 'F':
            listOfRows = listOfRows[0:int(len(listOfRows)/2)]

        else:
            listOfRows = listOfRows[int(len(listOfRows)/2):]

    return listOfRows[0]


def findColumn(file):
    listOfColumns = [x for x in range(0, 8)]

    for i in range(7, 10):
        if file[i] == 'L':
            listOfColumns = listOfColumns[0:int(len(listOfColumns)/2)]

        else:
            listOfColumns = listOfColumns[int(len(listOfColumns)/2):]

    return listOfColumns[0]


def getSeatIds(inputFile):
     with open(inputFile, 'r') as file:
        fileInput = file.readlines()
        listOfIds = []

        for line in fileInput:
            listOfIds.append(findRow(line.strip()) * 8 + findColumn(line.strip()))

        return listOfIds


def findMySeat(listOfSeatIds):
    
    for i in range(min(listOfSeatIds), max(listOfSeatIds)):
        if i not in listOfSeatIds:
            print(i)
        

findMySeat(getSeatIds('input.txt'))