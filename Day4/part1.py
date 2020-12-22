
# https://adventofcode.com/2020/day/4


import re


def findValidPassports(inputFile):
    with open(inputFile, 'r') as file:
        fileInput = file.readlines()
        passports = ['']
        counter = 0
        pattern = '(ecl|pid|eyr|hcl|byr|iyr|hgt)'

        for line in fileInput:
            if line.replace('\n', '') == '':
                counter += 1
                passports.append('')

            passports[counter] += line.replace('\n', ' ')

        correctPassports = filter(lambda x: len(
            set(re.findall(pattern, x.strip()))) == 7, passports)

    return list(correctPassports)


print(len(findValidPassports('input.txt')))
