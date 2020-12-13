import operator

class Instruction:
    def __init__(self, instruction, sign, value):
        self.instruction = instruction
        self.sign = sign
        self.value = int(value)
        self.executed = False

operators = {
    '+': operator.add,
    '-': operator.sub,
}

program = []
accumulator = 0

with open("../input/input.txt") as file:
   for line in file:
       ln = line.split()
       entry = Instruction(ln[0], ln[1][:1], ln[1][1:])
       program.append(entry)

i = 0
while not program[i].executed:
    program[i].executed = True
    instruction = program[i].instruction
    op = program[i].sign
    value = program[i].value

    if instruction == "nop":
        i += 1
    elif instruction == "acc":
        accumulator = operators.get(op)(accumulator, value)
        i += 1
    elif instruction == "jmp":
        i = operators.get(op)(i, value)

print("acc at point of infinit loop:", accumulator)
    