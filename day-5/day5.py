def pos(op, ops, index, pointer):
    if len(str(op)) < abs(index) or str(op)[index] == "0":
        return ops[pointer - index - 2]
    return pointer - index - 2


def intcode(program, test_id):
    ops = [int(i) for i in program.split(",")]
    i = 0
    while i <= len(ops):
        op = ops[i]
        if op == 99:
            return ",".join([str(x) for x in ops])

        n1 = int(ops[pos(op, ops, -3, i)])
        try:
            n2 = int(ops[pos(op, ops, -4, i)])
        except:
            pass

        if str(op)[-1] == "1":
            ops[ops[i + 3]] = n1 + n2
            i = i + 4
        elif str(op)[-1] == "2":
            ops[ops[i + 3]] = n1 * n2
            i = i + 4
        elif str(op)[-1] == "3":
            ops[ops[i + 1]] = test_id
            i += 2
        elif str(op)[-1] == "4":
            print(n1)
            i += 2
        elif str(op)[-1] == "5":
            if n1 != 0:
                i = n2
            else:
                i += 3
        elif str(op)[-1] == "6":
            if n1 == 0:
                i = n2
            else:
                i += 3
        elif str(op)[-1] == "7":
            if n1 < n2:
                ops[ops[i + 3]] = 1
            else:
                ops[ops[i + 3]] = 0
            i += 4
        elif str(op)[-1] == "8":
            if n1 == n2:
                ops[ops[i + 3]] = 1
            else:
                ops[ops[i + 3]] = 0
            i += 4
        else:
            print("Invalid op")
            return


def TEST(test_id):
    with open("day-5/input.txt") as data:
        program = data.read()
        intcode(program, test_id)


print("PART 1:")
TEST(1)
print("PART 2:")
TEST(5)
