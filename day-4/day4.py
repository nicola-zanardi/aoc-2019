def pw_check(pw):
    pw = list(str(pw))
    for i in range(1, len(pw)):
        if pw[i - 1] > pw[i]:
            return False
    if len(set(pw)) == len(pw):
        return False
    doubles = [digit for digit in pw if pw.count(digit) > 1]
    ok_doubles = 0
    for double in doubles:
        if pw[pw.index(double)] == pw[pw.index(double) + 1]:
            # addition for part 2
            if (
                len(pw) - 1 == pw.index(double) + 1
                or pw[pw.index(double) + 1] != pw[pw.index(double) + 2]
            ):
                ok_doubles += 1
    return ok_doubles > 0


n = 0
for pw in range(147981, 691423 + 1):
    if pw_check(pw):
        n += 1
print(n)

