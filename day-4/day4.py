def part1(pw):
    digits = list(str(pw))
    for i in range(1, len(digits)):
        if digits[i - 1] > digits[i]:
            return False
    if len(set(digits)) == len(digits):
        return False
    doubles = [digit for digit in digits if digits.count(digit) > 1]
    ok_doubles = 0
    for double in doubles:
        if digits[digits.index(double)] == digits[digits.index(double) + 1]:
            ok_doubles += 1
    return ok_doubles > 0


n = 0
for pw in range(147981, 691423 + 1):
    if part1(pw):
        n += 1
print(n)

