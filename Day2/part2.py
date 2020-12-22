
# https://adventofcode.com/2020/day/2


def validatePassword(inputLine):

    rangeTuple = (int(inputLine[0:inputLine.index('-')])-1,
                  int(inputLine[inputLine.index('-')+1:inputLine.index(' ')])-1)

    letterToCheck = inputLine[inputLine.index(' ')+1:inputLine.index(':')]

    password = inputLine[inputLine.index(':')+2:]

    if password[rangeTuple[0]] == letterToCheck and password[rangeTuple[1]] != letterToCheck or password[rangeTuple[0]] != letterToCheck and password[rangeTuple[1]] == letterToCheck:
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
