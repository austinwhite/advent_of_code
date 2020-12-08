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

        if all is not None:
            self.fill_info_from_list(all)
    
    def info_is_complete(self, optional=[]):
        for key, value in self.info.items():
            if value is None and key not in optional:
                return False
        return True

    def print_info(self, frame=False, omit=[]):
        if frame:
            print("-------------")
        for key, value in self.info.items():
            if key not in omit:
                print(key, ":", value)
        if frame:
            print("-------------")

    def set_info_field(self, field, value):
        if field in self.info:
            self.info[field] = value
    
    def fill_info_from_list(self, fields):
        for field in fields:
            self.set_info_field(field[0], field[1])


def make_new_passport(list):
    new_passport = Passport(all=list)
    return new_passport

passports = []

with open("../input/input.txt") as file:
    curr_info = []
    for line in file:
        if line == "\n" or line == None:
            passports.append(make_new_passport(curr_info))
            curr_info = []
        else:
            fields = line.split()
            for field in fields:
                curr_info.append(field.split(":"))

valid_passports = 0

for passport in passports:
    if passport.info_is_complete(optional=["cid"]):
        valid_passports += 1

print(valid_passports)