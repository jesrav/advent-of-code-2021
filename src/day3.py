
from typing import List

import numpy as np


test_data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def read_input(fpath: str) -> List[str]:
    with open(fpath) as f:
        return [line.replace('\n', '') for line in f.readlines()]


def parse_input(raw_input_data: List[str]) -> np.array:
    return np.array([list(s) for s in raw_input_data]).astype(int)


def get_gama_binary_rate(input_data: np.array) -> list[int]:
    input_length = input_data.shape[0]
    one_most_common = input_data.sum(axis=0) > (input_length / 2)
    return (1*one_most_common).tolist()
    

def epsilon_rate_from_gamma_rata(gamma_rate: list[int]) -> list[int]:
    return [1 - bit for bit in gamma_rate]


def binary_list_to_number(binary_list: list[int]) -> int:
    binary_str = "".join([str(bit) for bit in binary_list])
    return int(binary_str, 2)


# Test case, part 1
input_test_data = parse_input(test_data)
gama_rate_binary = get_gama_binary_rate(input_test_data)
empsilon_rate_binary = epsilon_rate_from_gamma_rata(gama_rate_binary)
assert binary_list_to_number(gama_rate_binary) * binary_list_to_number(empsilon_rate_binary) == 198


if __name__ == "__main__":

    raw_input_data = read_input("data/day3.txt")

    # Part 1
    input_data = parse_input(raw_input_data)
    gama_rate_binary = get_gama_binary_rate(input_data)
    epsilon_rate_binary = epsilon_rate_from_gamma_rata(gama_rate_binary)
    part1_answer = binary_list_to_number(gama_rate_binary) * binary_list_to_number(epsilon_rate_binary)
    print(f"Part 1: {part1_answer}")
