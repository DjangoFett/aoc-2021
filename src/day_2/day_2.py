def get_position(positions):
    depth = 0
    horizontal_position = 0

    for direction, magnitude in positions:
        if direction == "forward":
            horizontal_position += magnitude
        if direction == "down":
            depth += magnitude
        if direction == "up":
            depth -= magnitude

    return depth * horizontal_position


def get_position_with_aim(positions):
    depth = 0
    horizontal_position = 0
    aim = 0

    for direction, magnitude in positions:
        if direction == "forward":
            horizontal_position += magnitude
            depth += magnitude * aim
        if direction == "down":
            aim += magnitude
        if direction == "up":
            aim -= magnitude

    return depth * horizontal_position
