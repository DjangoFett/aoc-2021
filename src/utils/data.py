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


def split_into_str_and_int(x):
    a, b = x.split(" ")
    return (str(a), int(b))


def split_string(item: str, delimiter: str, types: list):
    return (types[i](x) for i, x in enumerate(item.split(delimiter)))


def split_string_into_chars(item: str, types: list):
    return [types[i](x) for i, x in enumerate(item)]


def split_input(items, func, **kwargs):
    return list(map(lambda x: func(x, **kwargs), items))
