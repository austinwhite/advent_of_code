class Position:
    direction_idx = {
        'N': 0,
        'E': 1,
        'S': 2,
        'W': 3,
    }

    directions = ['N', 'E', 'S', 'W']

    def __init__(self):
        self.facing = 'E'
        self.position = {
            'N': 0,
            'E': 0,
            'S': 0,
            'W': 0,
        }

    def rotate(self, direction, degree):
        i = self.direction_idx.get(self.facing)
        if direction == "R":
            self.facing = self.directions[(i + degree//90) % len(self.directions)]
        else:
            self.facing = self.directions[(i - degree//90) % len(self.directions)]

    def move(self, direction, distance):
        if direction == 'F':
            self.position[self.facing] += distance
        else:
            self.position[direction] += distance

    def manhattin_distance(self):
        x = abs(self.position.get('W') - self.position.get('E'))
        y = abs(self.position.get('N') - self.position.get('S'))
        return x + y

ship = Position()

with open("../input/input.txt") as file:
    for line in file:
        direction = line[0]
        distance = int(line[1:])
        if direction == 'L' or direction == 'R':
            ship.rotate(direction, distance)
        else:
            ship.move(direction, distance)

print("manhattin distance:", ship.manhattin_distance())