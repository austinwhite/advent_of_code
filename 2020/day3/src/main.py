def trees_hit(slope, move_x, move_y):
    curr_x = 0
    curr_y = 0
    trees_hit = 0

    while curr_y < len(slope):
        if slope[curr_y][curr_x] == '#':
            trees_hit += 1
        if curr_x + move_x > len(slope[0])-1:
            curr_x = move_x - (len(slope[0]) - curr_x)
        else:
            curr_x += move_x
        curr_y += move_y

    return trees_hit

def trees_hit_multiple_inputs(slope, inputs):
    total_trees = 1
    for element in inputs:
        total_trees *= trees_hit(slope, element[0], element[1])
    return total_trees

slope = []
inputs = [[1,1], [3,1], [5,1], [7,1], [1,2]]

with open("../input/input.txt") as file:
    for line in file:
        slope.append([char for char in line][:-1])

print("Trees hit:", trees_hit(slope, 3, 1))
print("Trees hit:", trees_hit_multiple_inputs(slope, inputs))