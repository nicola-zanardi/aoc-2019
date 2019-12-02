import math

def fuel_calculator(mass):
    return math.floor(mass/3) - 2

def part1():
    total_fuel = 0
    with open('input.txt') as data:
        for module in data:
            total_fuel = total_fuel + fuel_calculator(int(module))
            
    return total_fuel

print("PART 1")
print(f"Total fuel needed: {part1()}")