
# https://adventofcode.com/2020/day/2


import re


def validatePassword(inputLine):

    rangeTuple = (int(inputLine[0:inputLine.index('-')]),
                  int(inputLine[inputLine.index('-')+1:inputLine.index(' ')]))

    letterToCheck = inputLine[inputLine.index(' ')+1:inputLine.index(':')]

    password = inputLine[inputLine.index(':')+2:]

    pattern = f'[{letterToCheck}]'

    if rangeTuple[0] <= len(re.findall(pattern, password)) <= rangeTuple[1]:
        return True

    return False


def findValidPasswords(inputFile):
    with open(inputFile, 'r') as file:
        ValidPasswords = 0
        passwords = file.readlines()

        for password in passwords:
            if validatePassword(password):
                ValidPasswords += 1

    return ValidPasswords


print(findValidPasswords('input.txt'))
