def read_data(filename):
    lines = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            lines.append(line)
    return lines


def cast_to_int(items):
    return list(map(lambda x: int(x), items))


def cast_to_string(items):
    return list(map(lambda x: str(x), items))


def split_into_tuple(x):
    a, b = x.split(" ")
    return (str(a), int(b))


def split_input(items, func):
    return list(map(lambda x: func(x), items))
