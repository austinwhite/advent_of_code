def binary_space_partition(bsp, i, lower, upper):
    if i == len(bsp)-1:
        return lower if bsp[i] == 'F' or bsp[i] == 'L' else upper
    middle = (lower+upper)//2
    if bsp[i] == 'F' or bsp[i] == 'L':
        return binary_space_partition(bsp, i+1, lower, middle)
    if bsp[i] == 'B' or bsp[i] == 'R':
        return binary_space_partition(bsp, i+1, middle+1, upper)

def find_free_seat(ID_list):
    curr = 1
    while curr < len(ID_list):
        my_potential_seat = ID_list[curr]+1
        if my_potential_seat != ID_list[curr+1]:
            break
        curr += 1
    return my_potential_seat

ID_list = []

with open("../input/input.txt") as file:
    for line in file:
        ID = binary_space_partition(line[:-4], 0, 0, 127)
        column = binary_space_partition(line[-4:], 0, 0, 7)
        ID_list.append((ID*8)+column)

ID_list.sort()

print("max seat ID:", ID_list[-1])
print("my seat ID:", find_free_seat(ID_list))
