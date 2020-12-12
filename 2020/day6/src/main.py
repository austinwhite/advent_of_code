#
#  PART 1
#
 
any_yes = 0
with open("../input/input.txt") as file:
    yes = {}
    for line in file:
        if line == "\n":
            yes = {}
        else:
            for char in line:
                if not yes.get(char) and char != '\n':
                    yes[char] = 1
                    any_yes += 1
                elif char in yes:
                    yes[char] += 1
                    
print("any yes:", any_yes)

#
#  PART 2
#

common_yes = 0
with open("../input/input.txt") as file:
    yes = {}
    new_block = True
    for line in file:
        if line == "\n":
            yes = {}
            new_block = True
        else:
            if new_block:
                new_block = False
                # dont include new line character
                common_yes += len(line[:-1])
                for char in line[:-1]:
                    yes[char] = True
            else:
                new_yes = yes.copy()
                for char in yes.keys():
                    if char not in line:
                        new_yes.pop(char)
                        common_yes -= 1
                yes = new_yes

print("common yes:", common_yes)