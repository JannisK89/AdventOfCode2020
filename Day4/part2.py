"""

"""

import re


def FindValidPassports(file):
    fileInput = open(file, 'r').readlines()
    passports = ['']
    counter = 0
    pattern = '(ecl|pid|eyr|hcl|byr|iyr|hgt)'

    for line in fileInput:
        if line.replace('\n', '') == '':
            counter += 1
            passports.append('')

        passports[counter] += line.replace('\n', ' ')

    correctPassports = filter(lambda x: len(re.findall(pattern, x.strip())) == 7, passports)

    return list(correctPassports)


def CreateDictionary(passportList):
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


def ValidateFields(dictionaryList):

    EYECOLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    PID_PATTERN = '[\d]{9}'
    HAIR_COLOR_PATTERN = '#[0-9a-f]{6}'
    valid = 0

    for dic in dictionaryList:

        # print(dic)
        #print(f'EYE COLOR: {dic["ecl"]}\nPID: {dic["pid"]}\nEXPIRATION DATE: {dic["eyr"]}\nHAIR COLOR: {dic["hcl"]}\nBIRTH YEAR: {dic["byr"]}\nHEIGHT: {dic["hgt"]}')

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

        if (re.fullmatch('[\d]{2}in', dic['hgt']) and int(dic['hgt'][:2]) in range(59, 76)) or ((re.fullmatch('[\d]{3}cm', dic['hgt']) and int(dic['hgt'][:3]) in range(150, 193))):
            valid += 1
            continue

    return valid


validPassports = FindValidPassports("testinput.txt")

print(f'Found {len(validPassports)} valid passports')

dictOfPassports = CreateDictionary(validPassports)

print(ValidateFields(dictOfPassports))
