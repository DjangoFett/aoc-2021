def get_number_of_depth_increases(lines):
    return sum(1 for i in range(1, len(lines)) if lines[i] > lines[i - 1])


def get_number_of_depth_increases_chunks(lines):
    chunks = [sum(lines[i : i + 3]) for i in range(0, len(lines))]
    return sum(1 for i in range(1, len(chunks)) if chunks[i] > chunks[i - 1])
