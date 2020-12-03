def trees_hit(mountain, move_x, move_y):
    curr_x = 0
    curr_y = 0
    trees_hit = 0

    while curr_y < len(mountain):
        if mountain[curr_y][curr_x] == '#':
            trees_hit += 1
        if curr_x + move_x > len(mountain[0])-1:
            curr_x = move_x - (len(mountain[0]) - curr_x)
        else:
            curr_x += move_x
        curr_y += move_y

    return trees_hit

def trees_hit_multiple_slopes(mountain, slopes):
    total_trees = 1
    for slope in slopes:
        total_trees *= trees_hit(mountain, slope[0], slope[1])
    return total_trees

mountain = []
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

with open("../input/input.txt") as file:
    for line in file:
        mountain.append([char for char in line][:-1])

print("Trees hit:", trees_hit(mountain, 3, 1))
print("Trees hit:", trees_hit_multiple_slopes(mountain, slopes))