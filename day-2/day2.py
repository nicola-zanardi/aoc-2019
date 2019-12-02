def intcode(program):
    instructions = [int(i) for i in program.split(",")]
    i = 0
    while i <= len(instructions):
        instruction = instructions[i]
        if instruction == 99:
            return ",".join([str(x) for x in instructions])
        elif instruction == 1:
            number_1 = instructions[instructions[i + 1]]
            number_2 = instructions[instructions[i + 2]]
            instructions[instructions[i + 3]] = number_1 + number_2
            i = i + 4
        elif instruction == 2:
            number_1 = instructions[instructions[i + 1]]
            number_2 = instructions[instructions[i + 2]]
            instructions[instructions[i + 3]] = number_1 * number_2
            i = i + 4
        else:
            print("Invalid opcode")
            return


def part_1():
    with open("input.txt") as data:
        program = data.read().split(",")
        program[1] = "12"
        program[2] = "2"
        return intcode(",".join(program)).split(",")[0]


def part_2():
    with open("input.txt") as data:
        data = data.read().split(",")

    for noun in range(0, 100):
        for verb in range(0, 100):
            program = data.copy()
            program[1] = str(noun)
            program[2] = str(verb)
            if intcode(",".join(program)).split(",")[0] == "19690720":
                return 100 * noun + verb
    return "ARGH!"


print(f"PART 1: {part_1()}")
print(f"PART 2: {part_2()}")
