from dataclasses import dataclass


@dataclass
class CardNumber:
    value: int
    drawn: bool = False

    def __init__(self, value):
        self.value = value


@dataclass
class Card:
    card: list[list[CardNumber]]
    raw_card: list[list[int]]
    bingo: bool = False

    def __init__(self, card):
        self.card = self.transform(card)
        self.raw_card = card

    def mark_number(self, number_drawn):
        for row in self.card:
            for card_number in row:
                if card_number.value == number_drawn:
                    card_number.drawn = True

    def check_for_bingo(self):
        if (self.check_row() or self.check_column()) and not self.bingo:
            self.bingo = True
            return True
        return False

    def check_row(self):
        for row in self.card:
            if all([card_number.drawn for card_number in row]):
                return True
        return False

    def check_column(self):
        for i in range(len(self.card[0])):
            if all([row[i].drawn for row in self.card]):
                return True
        return False

    def get_score(self, last_number_drawn):
        unmarked_sum = 0

        for row in self.card:
            for card_number in row:
                if not card_number.drawn:
                    unmarked_sum += card_number.value

        return last_number_drawn * unmarked_sum

    @staticmethod
    def transform(card):
        return [[CardNumber(value) for value in row] for row in card]


def play_bingo_to_win(turns, cards):
    cards = [Card(card) for card in cards]
    for turn in turns:
        for card in cards:
            card.mark_number(turn)
            if card.check_for_bingo():
                return card.get_score(turn)
    return 0


def play_bingo_to_lose(turns, cards):
    cards = [Card(card) for card in cards]
    losing_score = 0
    for turn in turns:
        for card in cards:
            card.mark_number(turn)
            if card.check_for_bingo():
                losing_score = card.get_score(turn)
    return losing_score
