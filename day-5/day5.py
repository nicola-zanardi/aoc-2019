def intcode(program, test_id):
    instructions = [int(i) for i in program.split(",")]
    i = 0
    while i <= len(instructions):
        instruction = instructions[i]
        p = -1
        if instruction == 99:
            return ",".join([str(x) for x in instructions])
        elif str(instruction)[-1] == "1":
            if len(str(instruction)) < 3 or str(instruction)[-3] == "0":
                number_1 = int(instructions[instructions[i + 1]])
            else:
                number_1 = int(instructions[i + 1])
            if len(str(instruction)) < 4 or str(instruction)[-4] == "0":
                number_2 = int(instructions[instructions[i + 2]])
            else:
                number_2 = int(instructions[i + 2])
            instructions[instructions[i + 3]] = number_1 + number_2
            i = i + 4
        elif str(instruction)[-1] == "2":
            if len(str(instruction)) < 3 or str(instruction)[-3] == "0":
                number_1 = int(instructions[instructions[i + 1]])
            else:
                number_1 = int(instructions[i + 1])
            if len(str(instruction)) < 4 or str(instruction)[-4] == "0":
                number_2 = int(instructions[instructions[i + 2]])
            else:
                number_2 = int(instructions[i + 2])
            instructions[instructions[i + 3]] = number_1 * number_2
            i = i + 4
        elif str(instruction)[-1] == "3":
            instructions[instructions[i + 1]] = test_id
            i += 2
        elif str(instruction)[-1] == "4":
            if len(str(instruction)) < 3 or str(instruction)[-3] == "0":
                print(instructions[instructions[i + 1]])
            else:
                print(instructions[i + 1])
            i += 2
        elif str(instruction)[-1] == "5":
            if len(str(instruction)) < 3 or str(instruction)[-3] == "0":
                number_1 = int(instructions[instructions[i + 1]])
            else:
                number_1 = int(instructions[i + 1])
            if len(str(instruction)) < 4 or str(instruction)[-4] == "0":
                number_2 = int(instructions[instructions[i + 2]])
            else:
                number_2 = int(instructions[i + 2])
            if number_1 != 0:
                i = number_2
            else:
                i += 3
        elif str(instruction)[-1] == "6":
            if len(str(instruction)) < 3 or str(instruction)[-3] == "0":
                number_1 = int(instructions[instructions[i + 1]])
            else:
                number_1 = int(instructions[i + 1])
            if len(str(instruction)) < 4 or str(instruction)[-4] == "0":
                number_2 = int(instructions[instructions[i + 2]])
            else:
                number_2 = int(instructions[i + 2])
            if number_1 == 0:
                i = number_2
            else:
                i += 3
        elif str(instruction)[-1] == "7":
            if len(str(instruction)) < 3 or str(instruction)[-3] == "0":
                number_1 = int(instructions[instructions[i + 1]])
            else:
                number_1 = int(instructions[i + 1])
            if len(str(instruction)) < 4 or str(instruction)[-4] == "0":
                number_2 = int(instructions[instructions[i + 2]])
            else:
                number_2 = int(instructions[i + 2])
            if number_1 < number_2:
                instructions[instructions[i + 3]] = 1
            else:
                instructions[instructions[i + 3]] = 0
            i += 4
        elif str(instruction)[-1] == "8":
            if len(str(instruction)) < 3 or str(instruction)[-3] == "0":
                number_1 = int(instructions[instructions[i + 1]])
            else:
                number_1 = int(instructions[i + 1])
            if len(str(instruction)) < 4 or str(instruction)[-4] == "0":
                number_2 = int(instructions[instructions[i + 2]])
            else:
                number_2 = int(instructions[i + 2])
            if number_1 == number_2:
                instructions[instructions[i + 3]] = 1
            else:
                instructions[instructions[i + 3]] = 0
            i += 4
        else:
            print("Invalid opcode")
            return


def TEST(test_id):
    with open("day-5/input.txt") as data:
        program = data.read()
        intcode(program, test_id)


print("PART 1:")
TEST(1)
print("PART 2:")
TEST(5)