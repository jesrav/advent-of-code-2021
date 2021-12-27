
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


def get_most_common_bits(input_data: np.array) -> list[int]:
    input_length = input_data.shape[0]
    one_most_common = input_data.sum(axis=0) >= (input_length / 2)
    return (1*one_most_common).tolist()
    

def least_common_bits_from_most_common(gamma_rate: list[int]) -> list[int]:
    return [1 - bit for bit in gamma_rate]


def binary_list_to_number(binary_list: list[int]) -> int:
    binary_str = "".join([str(bit) for bit in binary_list])
    return int(binary_str, 2)


def filter_bits(input_data: np.array, filter_on_least_common: bool = False) -> List[int]:
    i = 0
    n_bits = input_data.shape[1] 
    rows = input_data.shape[0]
    filtered_input = input_data.copy()
    while rows > 1 and i < n_bits:
        filter_list = get_most_common_bits(filtered_input)
        if filter_on_least_common:
            filter_list = least_common_bits_from_most_common(filter_list)
        equal_to_filter_at_i = filtered_input[:, i] == filter_list[i]
        filtered_input = filtered_input[equal_to_filter_at_i]
        i += 1
        rows = filtered_input.shape[0]
    return filtered_input.tolist()[0]


# Test case, part 1
input_test_data = parse_input(test_data)
gama_rate_binary = get_most_common_bits(input_test_data)
empsilon_rate_binary = least_common_bits_from_most_common(gama_rate_binary)
assert binary_list_to_number(gama_rate_binary) * binary_list_to_number(empsilon_rate_binary) == 198

# Test case, part 2
oxigen_generator_rating = filter_bits(input_test_data)
co2_scrubber_rating = filter_bits(input_test_data, filter_on_least_common=True)
assert binary_list_to_number(oxigen_generator_rating) * binary_list_to_number(co2_scrubber_rating) == 230

if __name__ == "__main__":

    raw_input_data = read_input("data/day3.txt")
    input_data = parse_input(raw_input_data)

    # Part 1
    gama_rate_binary = get_most_common_bits(input_data)
    epsilon_rate_binary = least_common_bits_from_most_common(gama_rate_binary)
    part1_answer = binary_list_to_number(gama_rate_binary) * binary_list_to_number(epsilon_rate_binary)
    print(f"Part 1: {part1_answer}")

    # Part 2
    oxigen_generator_rating = filter_bits(input_data)
    co2_scrubber_rating = filter_bits(input_data, filter_on_least_common=True)
    part2_answer = binary_list_to_number(oxigen_generator_rating) * binary_list_to_number(co2_scrubber_rating)
    print(f"Part 2: {part2_answer}")