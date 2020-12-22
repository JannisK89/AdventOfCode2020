
# https://adventofcode.com/2020/day/6


def findSimilarAnswers(inputFile):
    with open(inputFile, 'r') as file:
        lines = file.readlines()
        group, total, counter = '', 0, 0

        for answer in lines:
            if answer.strip() != '':
                group += answer.strip()
                counter += 1
                
            else:
                total += calculateSimilar(group, counter)
                group, counter = '', 0

        total += calculateSimilar(group, counter)
        return total


def calculateSimilar(groupStr, counter):
    returnValue = 0
    for value in set(groupStr):
        if groupStr.count(value) == counter:
            returnValue += int(groupStr.count(value) / counter)
    return returnValue


print(findSimilarAnswers('input.txt'))
