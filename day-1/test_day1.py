from day1 import fuel_calculator


def test_part1_1():
    assert fuel_calculator(12) == 2


def test_part1_2():
    assert fuel_calculator(14) == 2


def test_part1_3():
    assert fuel_calculator(1969) == 654


def test_part1_3():
    assert fuel_calculator(100756) == 33583
