from day1 import fuel_calculator, fuel_calculator_improved


def test_part1_1():
    assert fuel_calculator(12) == 2


def test_part1_2():
    assert fuel_calculator(14) == 2


def test_part1_3():
    assert fuel_calculator(1969) == 654


def test_part1_3():
    assert fuel_calculator(100756) == 33583


def test_part2_1():
    assert fuel_calculator_improved(14) == 2


def test_part2_2():
    assert fuel_calculator_improved(1969) == 966


def test_part2_3():
    assert fuel_calculator_improved(100756) == 50346
