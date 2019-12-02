import math


def fuel_calculator(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel < 0:
        return 0
    return fuel


def part1():
    total_fuel = 0
    with open("input.txt") as data:
        for module in data:
            total_fuel = total_fuel + fuel_calculator(int(module))

    return total_fuel


def fuel_calculator_improved(mass):
    fuel = fuel_calculator(mass)
    if fuel == 0:
        return fuel
    return fuel + fuel_calculator_improved(fuel)


def part2():
    total_fuel = 0
    with open("input.txt") as data:
        for module in data:
            total_fuel = total_fuel + fuel_calculator_improved(int(module))

    return total_fuel


print("PART 1")
print(f"Total fuel needed: {part1()}")
print("PART 2")
print(f"Total fuel needed: {part2()}")
