
# https://adventofcode.com/2020/day/3


def countTrees(inputFile, xAcc, yAcc):
    with open(inputFile, 'r') as file:
        map = file.readlines()
        trees = 0
        xPos = 0

        for line in range(yAcc, len(map), yAcc):
            lineStripped = map[line].replace('\n', '')
            xPos += xAcc

            if lineStripped[xPos] == '#':
                trees += 1

            if xPos + xAcc >= len(lineStripped):
                xPos -= len(lineStripped)

    return trees


def calculateTotal(slopes):
    total = 1
    for slope in slopes:
        total *= countTrees('input.txt', slope[0], slope[1])

    return total


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(calculateTotal(slopes))
