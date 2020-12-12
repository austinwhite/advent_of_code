import re

class Passport:
    def __init__(self, all=None, byr=None, iyr=None, eyr=None, 
                    hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.info = {
            "byr": byr,
            "iyr": iyr,
            "eyr": eyr,
            "hgt": hgt,
            "hcl": hcl,
            "ecl": ecl,
            "pid": pid,
            "cid": cid,
        }

        self.info_format = {
            "byr": "^[0-9]{4}$",
            "iyr": "^[0-9]{4}$",
            "eyr": "^[0-9]{4}$",
            "hgt": "^[0-9]+[incm]{2}$",
            "hcl": "^[#][0-9a-f]{6}$",
            "ecl": "^amb|blu|brn|gry|grn|hzl|oth$",
            "pid": "^[0-9]{9}$",
            "cid": None,
        }

        if all is not None:
            self.__fill_info_from_list(all)
    
    def info_is_valid(self, check_format=False, optional=[]):
        for key, value in self.info.items():
            if value is None and key not in optional or check_format is True and not self.__check_info_format(key):
                return False
        return True

    def __check_info_format(self, field):
        if field == "cid":
            return True
        valid = False
        pattern = re.compile(self.info_format[field])
        valid = bool(pattern.match(self.info[field]))
        if valid and field == "byr":
            valid = 1920 <= int(self.info["byr"]) <= 2002
        elif valid and field == "iyr":
            valid = 2010 <= int(self.info["iyr"]) <= 2020
        elif valid and field == "eyr":
            valid = 2020 <= int(self.info["eyr"]) <= 2030
        elif valid and field == "hgt":
            val = self.info[field][:-2]
            unit = self.info[field][-2:]
            if unit == "cm":
                valid = 150 <= int(val) <= 193
            elif unit == "in":
                valid = 59 <= int(val) <= 76
            else:
                valid = False
        return valid

    def __set_info_field(self, field, value):
        if field in self.info:
            self.info[field] = value
    
    def __fill_info_from_list(self, fields):
        for field in fields:
            self.__set_info_field(field[0], field[1])


def make_new_passport(list):
    new_passport = Passport(all=list)
    return new_passport

passports = []

with open("../input/input.txt") as file:
    curr_info = []
    for line in file:
        if line == "\n":
            passports.append(make_new_passport(curr_info))
            curr_info = []
        else:
            fields = line.split()
            for field in fields:
                curr_info.append(field.split(":"))

valid_passports = 0
valid_formats = 0

for passport in passports:
    if passport.info_is_valid(optional=["cid"]):
        valid_passports += 1
    if passport.info_is_valid(optional=["cid"], check_format=True):
        valid_formats += 1

print("complete info:", valid_passports)
print("with correct format:", valid_formats)