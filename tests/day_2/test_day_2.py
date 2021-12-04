from src.utils.data import read_data
from src.utils.data import split_into_str_and_int
from src.utils.data import split_input
from src.utils.data import split_string

from src.day_2.day_2 import get_position
from src.day_2.day_2 import get_position_with_aim


def test_get_position_sample():
    lines = read_data("fixtures/day_2/test.txt")
    parsed_input = split_input(lines, split_into_str_and_int)
    assert get_position(parsed_input) == 150


def test_get_position_input():
    lines = read_data("fixtures/day_2/input.txt")
    parsed_input = split_input(lines, split_into_str_and_int)
    assert get_position(parsed_input) == 1459206


def test_get_position_with_aim_sample():
    lines = read_data("fixtures/day_2/test.txt")
    parsed_input = split_input(lines, split_into_str_and_int)
    assert get_position_with_aim(parsed_input) == 900


def test_get_position_with_aim_input():
    lines = read_data("fixtures/day_2/input.txt")
    parsed_input = split_input(lines, split_string, delimiter=" ", types=[str, int])
    assert get_position_with_aim(parsed_input) == 1320534480
