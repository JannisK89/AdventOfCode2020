
# # https://adventofcode.com/2020/day/1


def findAndMultiply(inputFile):
    with open(inputFile, 'r') as file:
        inputList = file.readlines()

        for firstNumber in inputList:
            for secondNumber in inputList:
                if int(firstNumber) + int(secondNumber) <= 2020:
                    for thirdNumber in inputList:
                        if int(firstNumber) + int(secondNumber) + int(thirdNumber) == 2020:
                            return int(firstNumber) * int(secondNumber) * int(thirdNumber)


print(findAndMultiply("input.txt"))
