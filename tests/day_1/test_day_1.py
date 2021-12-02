from src.day_1.day_1 import get_number_of_depth_increases
from src.day_1.day_1 import get_number_of_depth_increases_chunks

from src.utils.data import read_data
from src.utils.data import cast_to_int


def test_count_of_depth_increases_sample():
    lines = cast_to_int(read_data("fixtures/day_1/test.txt"))
    assert get_number_of_depth_increases(lines) == 7


def test_count_of_depth_increases_real():
    lines = cast_to_int(read_data("fixtures/day_1/input.txt"))
    assert get_number_of_depth_increases(lines) == 1692


def test_count_of_depth_increases_chunks_sample():
    lines = cast_to_int(read_data("fixtures/day_1/test.txt"))
    assert get_number_of_depth_increases_chunks(lines) == 5


def test_count_of_depth_increases_chunks_real():
    lines = cast_to_int(read_data("fixtures/day_1/input.txt"))
    assert get_number_of_depth_increases_chunks(lines) == 1724
