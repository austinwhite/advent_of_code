import re

def is_valid_passowrd_policy1(min, max, letter, password):
    letter_count = 0
    for char in password:
        if char == letter:
            letter_count += 1
    return min <= letter_count <= max

def is_valid_passowrd_policy2(position1, position2, letter, password):
    first = password[position1-1] is letter
    second = password[position2-1] is letter
    return first != second

total_valid_passwords_policy1 = 0
total_valid_passwords_policy2 = 0

with open("../input/input.txt") as file:
    for line in file:
        min, max, letter, password = filter(None, re.split(r'[-:]|\s', line))
        if is_valid_passowrd_policy1(int(min), int(max), letter, password):
            total_valid_passwords_policy1 += 1
        if is_valid_passowrd_policy2(int(min), int(max), letter, password):
            total_valid_passwords_policy2 += 1

print("Policy1:", total_valid_passwords_policy1)
print("Policy2:", total_valid_passwords_policy2)