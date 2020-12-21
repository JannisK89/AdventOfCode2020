

# https://adventofcode.com/2020/day/4


import re


# Filter away all passports without the right fields
def findValidPassports(file):
    fileInput = open(file, 'r').readlines()
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


# Creates a list of dictionaries for each passport, making field look up easy
def createDictionary(passportList):
    listOfDictionaries = []
    counter = 0

    for passport in passportList:
        listOfDictionaries.append({})

        splitPassport = passport.strip().split(' ')

        for partOfPass in splitPassport:
            listOfDictionaries[counter].update(
                {partOfPass[0:partOfPass.index(':')]: partOfPass[partOfPass.index(':')+1::]})

        counter += 1

    return listOfDictionaries


# Filter away passports with invalid field data
def validateFields(dictionaryList):

    EYECOLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    PID_PATTERN = '[\\d]{9}'
    HAIR_COLOR_PATTERN = '#[0-9a-f]{6}'
    HEIGHT_INCHES_PATTERN = '[\\d]{2}in'
    HEIGHT_CENTIMETERS_PATTERN = '[\\d]{3}cm'
    valid = 0

    for dic in dictionaryList:

        if dic['ecl'] not in EYECOLORS:
            continue

        if re.fullmatch(PID_PATTERN, dic['pid']) is None:
            continue

        if 2020 > int(dic['eyr']) < 2030:
            continue

        if re.fullmatch(HAIR_COLOR_PATTERN, dic['hcl']) is None:
            continue

        if 1920 > int(dic['byr']) < 2002:
            continue

        if 2010 > int(dic['iyr']) < 2020:
            continue

        if (re.fullmatch(HEIGHT_INCHES_PATTERN, dic['hgt']) and int(dic['hgt'][:2]) in range(59, 76)) or ((re.fullmatch(HEIGHT_CENTIMETERS_PATTERN, dic['hgt']) and int(dic['hgt'][:3]) in range(150, 193))):
            valid += 1

    return valid


print(validateFields(createDictionary(findValidPassports("input.txt"))))
