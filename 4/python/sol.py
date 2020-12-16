import re
with open('input.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]

with open('test.txt', 'r') as f:
    test_data = [l.strip() for l in f.readlines()]


def parse_passport_data(data):
    passports = []
    passport = {}
    for line in data:
        if line:
            passport.update({k:v for k,v in [elem.split(':') for elem in line.split(' ')]})
        else:
            passports.append(passport)
            passport = {}
            continue
    passports.append(passport)
    return passports

passports = parse_passport_data(data)
test_passports = parse_passport_data(test_data)
assert len(test_passports) == 4

def validate_fields(passport, fields, optionals):
    missing = fields - set(passport.keys())
    return int(not missing or missing == optionals)


def validate_hgt(hgt):
    res = False
    if not (hgt.endswith('cm') or hgt.endswith('in')):
        return
    height, unit = int(hgt[:-2]), hgt[-2:]
    if unit == 'cm':
        res = 150 <= height <= 193
    elif unit == 'in':
        res = 59 <= height <= 76
    return res

assert validate_hgt('180cm') == True
assert validate_hgt('76in') == True

def validate_data(passport, fields, optionals):
    if not validate_fields(passport, set(fields.keys()), optionals):
        return 0
    for key, checker in fields.items():
        if not checker(passport[key]):
            return 0
    return 1


# Part1
ecls = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
req_fields = {
 'byr': lambda x: 1920 <= int(x) <= 2002,
 'iyr': lambda x: 2010 <= int(x) <= 2020,
 'eyr': lambda x: 2020 <= int(x) <= 2030,
 'hgt': validate_hgt,
 'hcl': lambda x: re.match(r'^#[0-9a-zA-Z]{6}$', x),
 'ecl': lambda x: x in ecls,
 'pid': lambda x: re.match(r'[0-9]{9}$', x),
}
optionals = {'cid'}
test_part1 = sum([validate_fields(p, set(req_fields.keys()), optionals) for p in test_passports])
assert test_part1 == 2

part1 = sum([validate_fields(p, set(req_fields.keys()), optionals) for p in passports])
assert part1 == 208
print(f'Part1 -> {part1}')

# Part2
test_part2 = sum([validate_data(p, req_fields, optionals) for p in test_passports])
assert test_part2 == 2
part2 = sum([validate_data(p, req_fields, optionals) for p in passports])
print(f'Part2 -> {part2}')
