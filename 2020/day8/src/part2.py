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

def copy_entry(entry):
    return Instruction(entry.instruction, entry.sign, entry.value)

def wipe_execution_history(instrucions):
    for instruction in instrucions:
        instruction.executed = False

def execute(program):
    accumulator = 0
    i = 0
    while i < len(program) and not program[i].executed:
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
    
    return -1 if i < len(program) else accumulator

def repair_program(program):
    swith_instruction = {
        "nop": "jmp",
        "jmp": "nop",
    }

    for i in range(len(program)):
        temp_entry = copy_entry(program[i])
        instruction = temp_entry.instruction
        if instruction == "nop" or instruction == "jmp":
            temp_entry.instruction = swith_instruction.get(instruction)
            accumulator = execute(program[:i] + [temp_entry] + program[i+1:])
            if accumulator > 0:
                return accumulator
            wipe_execution_history(program)

    return False

program = []

with open("../input/input.txt") as file:
   for line in file:
       ln = line.split()
       entry = Instruction(ln[0], ln[1][:1], ln[1][1:])
       program.append(entry)

print("acc after repairing:", repair_program(program))