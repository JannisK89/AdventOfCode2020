
# https://adventofcode.com/2020/day/6


def countDifferentAnswers(inputFile):
    with open(inputFile, 'r') as file:
        lines = file.readlines()
        group, total = '', 0

        for answer in lines:
            if answer.strip() != '':
                group += answer.strip()

            else:
                total += (len(set(group)))
                group = ''

        total += (len(set(group)))
        return total


print(countDifferentAnswers('input.txt'))
