def get_two(array, k):
    tab = {}
    for num in array:
        if tab.get(num):
            return [num, tab[num]]
        else:
            tab[k-num] = num
    return None

def get_three(array, k):
    for i in range(len(array)-2):
        newK = k - array[i]
        for j in range(i+1, len(array)-2):
            pair = get_two(array[j:], newK)
            if pair:
                return [array[i], pair[0], pair[1]]
    return None

def printAnswer(array, k):
    if array is None:
        return
    total = 0
    for val in array:
        if total == 0:
            total += val
        else:
            total *= val
    print("The", len(array), "numbers that sum up to",
                        k, "are", str(array), "=>", total)

array = []
sumTo = 2020
with open("../input/input.txt") as file:
    for line in file.readlines():
        array.append(int(line))

printAnswer(get_two(array, sumTo), sumTo)
printAnswer(get_three(array, sumTo), sumTo)
