from src.day_4.day_4 import play_bingo_to_win, play_bingo_to_lose
from src.utils.data import get_bingo_data


def test_play_bingo_to_win_sample():
    turns, boards = get_bingo_data("fixtures/day_4/test.txt")
    assert play_bingo_to_win(turns, boards) == 4512


def test_play_bingo_to_win():
    turns, boards = get_bingo_data("fixtures/day_4/input.txt")
    assert play_bingo_to_win(turns, boards) == 10374


def test_play_bingo_to_lose_sample():
    turns, boards = get_bingo_data("fixtures/day_4/test.txt")
    assert play_bingo_to_lose(turns, boards) == 1924


def test_play_bingo_to_lose():
    turns, boards = get_bingo_data("fixtures/day_4/input.txt")
    assert play_bingo_to_lose(turns, boards) == 24742
