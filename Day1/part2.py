"""
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. 
They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""


def FindAndMultiply(file):
    inputList = open(file, 'r').readlines()

    for firstNumber in inputList:
        for secondNumber in inputList:
            if int(firstNumber) + int(secondNumber) <= 2020:
                for thirdNumber in inputList:
                    if int(firstNumber) + int(secondNumber) + int(thirdNumber) == 2020:
                        return int(firstNumber) * int(secondNumber) * int(thirdNumber)


print(FindAndMultiply("input.txt"))
