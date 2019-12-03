# Lets' define some coordinates
# Starting point should be x=0 y=0
# After, let's follow the carthesian coordinates and increase up-right.


def compute_position(movement: str, starting_point):
    direction = movement[0]
    distance = int(movement[1:])

    sign = 1
    if direction == "D" or direction == "L":
        sign = -1

    if direction == "U" or direction == "D":
        return [
            (starting_point[0], starting_point[1] + sign * step)
            for step in range(1, distance + 1)
        ]
    return [
        (starting_point[0] + sign * step, starting_point[1])
        for step in range(1, distance + 1)
    ]


def distance(position):
    return abs(position[0]) + abs(position[1])


def get_positions_list(movements: str):
    positions = [(0, 0)]
    movements = movements.split(",")
    for movement in movements:
        positions.extend(compute_position(movement, positions[-1]))
    return positions


def find_intersections(positions_1, positions_2):
    return list(set(positions_1[1:]).intersection(positions_2))


def part_1(movements_cable_1, movements_cable_2):
    intersections = find_intersections(
        get_positions_list(movements_cable_1), get_positions_list(movements_cable_2)
    )
    return min([distance(intersection) for intersection in intersections])


if __name__ == "__main__":
    with open("input.txt") as data:
        coordinates = data.readlines()

    coordinates = [coordinate.strip() for coordinate in coordinates]

    print(f"PART 1: {part_1(*coordinates)}")
