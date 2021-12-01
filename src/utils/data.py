def read_data(filename):
    lines = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            lines.append(int(line))
    return lines
