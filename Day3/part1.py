
# https://adventofcode.com/2020/day/3


def countTrees(inputFile):
    with open(inputFile, 'r') as file:
        map = file.readlines()
        map.pop(0)
        xPos = 0
        trees = 0

        for line in map:
            lineStripped = line.replace('\n', '')
            xPos += 3

            if lineStripped[xPos] == '#':
                trees += 1

            if xPos+3 >= len(lineStripped):
                xPos -= len(lineStripped)

    return trees


print(countTrees('input.txt'))
