from src.utils.data import read_data, split_input, split_string_into_chars
from src.day_3.day_3 import get_diagnostic_report, get_o2_and_co2


def test_get_diagnostics_sample():
    lines = read_data("fixtures/day_3/test.txt")
    types = [int for _ in range(5)]
    parsed_input = split_input(lines, split_string_into_chars, types=types)
    assert get_diagnostic_report(parsed_input) == 198


def test_get_diagnostics_input():
    lines = read_data("fixtures/day_3/input.txt")
    types = [int for _ in range(12)]
    parsed_input = split_input(lines, split_string_into_chars, types=types)
    get_diagnostic_report(parsed_input) == 4006064


def test_get_o2_and_co2_sample():
    lines = read_data("fixtures/day_3/test.txt")
    types = [int for _ in range(5)]
    parsed_input = split_input(lines, split_string_into_chars, types=types)
    get_o2_and_co2(parsed_input) == 230


def test_get_o2_and_co2_input():
    lines = read_data("fixtures/day_3/input.txt")
    types = [int for _ in range(12)]
    parsed_input = split_input(lines, split_string_into_chars, types=types)
    get_o2_and_co2(parsed_input) == 5941884
