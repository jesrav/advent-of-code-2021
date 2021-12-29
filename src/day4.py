from typing import List
from itertools import groupby

import numpy as np


raw_test_data = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "",
    "22 13 17 11 0",
    "8 2 23 4 24",
    "21 9 14 16 7",
    "6 10 3 18 5",
    "1 12 20 15 19",
    "",
    "3 15 0 2 22",
    "9 18 13 17 5",
    "19 8 7 25 23",
    "20 11 10 24 4",
    "14 21 16 12 6",
    "",
    "14 21 17 24 4",
    "10 16 15 9 19",
    "18 8 23 26 20",
    "22 11 13 6 5",
    "2 0 12 3 7",
]


def read_input(fpath: str) -> List[str]:
    with open(fpath) as f:
        return [line.replace('\n', '') for line in f.readlines()]


class Board:
    def __init__(self, board_numbers: np.array) -> None:
        self.board_numbers = board_numbers
        self.board_markings = np.zeros(self.board_numbers.shape, dtype=bool)
        self.numbers_called = []

    def mark_number(self, number):
        self.board_markings = np.where(self.board_numbers == number,  True, self.board_markings)
        self.numbers_called.append(number)

    @property
    def has_winning_row(self):
        return (
            any(self.board_markings.sum(axis=0) == self.board_markings.shape[0])
            | any(self.board_markings.sum(axis=1) == self.board_markings.shape[1])
        )

    @property
    def score(self):
        marked_numbers_zeroed = np.where(self.board_markings == True, 0, self.board_numbers)
        return sum(sum(marked_numbers_zeroed)) * self.numbers_called[-1]

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.board_numbers == other.board_numbers).all()
        else:
            return False

class Bingo:

    def __init__(self, number_sequence: List[int], boards: List[Board]) -> None:
        self.number_sequence = number_sequence
        self.boards = boards
        self.winning_boards = []

    @property
    def boards_left(self):
        return [b for b in self.boards if b not in self.winning_boards]

    def call_number(self, number: int) -> None:
        for board in self.boards_left:
            board.mark_number(number)

    def play(self) -> int:
        for number in self.number_sequence:
            self.call_number(number)
            if len(self.boards_left) == 0:
                break

            for board in self.boards_left:
                if board.has_winning_row:
                    self.winning_boards.append(board)

    @staticmethod
    def parse_single_board_line(board_line: str) -> list[int]:
        return [int(n) for n in board_line.split(" ") if n != ""]

    @classmethod
    def from_raw_input(cls, raw_input_data: List[str]) -> 'Bingo':
        input_split_on_blank = [
            list(sub) for el, sub in groupby(raw_input_data, key=bool) if el
        ]
        number_sequence_str = input_split_on_blank[0][0]
        number_sequence = [int(n) for n in number_sequence_str.split(",")]

        boards = []
        for board_data in input_split_on_blank[1:]:
            boards.append(
                Board(board_numbers=np.array([cls.parse_single_board_line(line) for line in board_data]))
            )

        return Bingo(
            number_sequence=number_sequence,
            boards=boards
        )


# Test part 1
bingo_test = Bingo.from_raw_input(raw_test_data)
bingo_test.play()
assert bingo_test.winning_boards[0].score == 4512

# Test part 2
assert bingo_test.winning_boards[-1].score == 1924

if __name__ == "__main__":

    raw_input_data = read_input("data/day4.txt")
    bingo = Bingo.from_raw_input(raw_input_data)
    bingo.play()
    print(f"Part 1: {bingo.winning_boards[0].score}")
    print(f"Part 2: {bingo.winning_boards[-1].score}")