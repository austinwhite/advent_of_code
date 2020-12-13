def check_for_pair(preamble, target):
    tab = {}
    for num in preamble:
        if tab.get(num):
            return [num, tab[num]]
        else:
            tab[target-num] = num
    return False

def find_first_invalid_value(values):
    for i in range(25, len(values)):
        if not check_for_pair(values[i-25:i], values[i]):
            return values[i], i

def find_encryption_weakness(values, target):
    for i in range(len(values)):
        contiguous_sum = 0
        for j in range(i, len(values)):
            contiguous_sum += values[j]
            if contiguous_sum == target:
                return min(values[i:j+1]) + max(values[i:j+1])

values = []

with open("../input/input.txt") as file:
    for line in file:
        values.append(int(line))

first_invalid, i = find_first_invalid_value(values)
encryption_weakness = find_encryption_weakness(values[:i], first_invalid)
print("first invalid value:", first_invalid)
print("encryption weakness:", encryption_weakness)