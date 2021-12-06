def read_data(filename):
    lines = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            lines.append(line)
    return lines


def read_raw_data(file_name):
    with open(file_name) as file:
        return file.read()


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


# This doesn't need to exist but ¯\_(ツ)_/¯
def split_string_func(
    item: str,
    delimiter: str,
    func,
):
    return func(item.split(delimiter))


def split_input(items, func, **kwargs):
    return list(map(lambda x: func(x, **kwargs), items))


def get_bingo_data(input_file):
    data = read_raw_data(input_file).split("\n\n")
    turns = split_string_func(data.pop(0), ",", cast_to_int)
    cards = list(
        map(
            lambda x: list(map(lambda x: cast_to_int(x.split()), x)),
            [x.split("\n") for x in data],
        )
    )
    return (turns, cards)
