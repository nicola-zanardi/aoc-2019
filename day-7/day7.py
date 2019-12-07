from itertools import permutations


def intcode(program, test_id, feedback=False, i=0):
    def pos(op, ops, index, pointer):
        if len(str(op)) < abs(index) or str(op)[index] == "0":
            try:
                return ops[pointer - index - 2]
            except:
                return 99
        return pointer - index - 2

    ops = [int(i) for i in program.split(",")]
    j = 0
    while i <= len(ops):
        op = ops[i]

        n1 = int(ops[pos(op, ops, -3, i)])
        try:
            n2 = int(ops[pos(op, ops, -4, i)])
        except:
            pass

        if op == 99:
            return [n1], ",".join([str(x) for x in ops]), i
        if str(op)[-1] == "1":
            ops[ops[i + 3]] = n1 + n2
            i = i + 4
        elif str(op)[-1] == "2":
            ops[ops[i + 3]] = n1 * n2
            i = i + 4
        elif str(op)[-1] == "3":
            ops[ops[i + 1]] = test_id[j]
            i += 2
            j += 1
        elif str(op)[-1] == "4":
            i += 2
            if not feedback:
                return n1
            return n1, ",".join([str(x) for x in ops]), i
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


program = open("day-7/input.txt").readline().strip()
seqs = list(permutations("43210"))
seqs_2 = list(permutations("98765"))

results = set()


def amplify(stages, program, settings, signal=0, stage=0):
    if stage == stages:
        return signal
    signal = intcode(program, [settings[stage], signal])
    return amplify(stages, program, settings, signal, stage + 1)


for seq in seqs:
    results.add(amplify(5, program, seq))
print(f"PART 1: {max(results)}")


def amplify_feedback(
    stages, programs, settings, pointers, signal=0, stage=0, last_result=0
):
    if isinstance(signal, list):
        return last_result

    if stage == stages:
        last_result = signal
        stage = 0

    if pointers[stage] == 0:
        call = [settings[stage], signal]
    else:
        call = [signal]
    signal, programs[stage], pointers[stage] = intcode(
        programs[stage], call, feedback=True, i=pointers[stage],
    )
    return amplify_feedback(
        stages, programs, settings, pointers, signal, stage + 1, last_result
    )


results = set()
for seq in seqs_2:
    # seq = [9, 7, 8, 5, 6]
    pointers = [0, 0, 0, 0, 0]
    programs = [program for i in range(5)]
    results.add(amplify_feedback(5, programs, seq, pointers))
print(f"PART 2: {max(results)}")
