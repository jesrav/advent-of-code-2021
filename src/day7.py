from typing import List

from common import read_input

raw_test_data = '16,1,2,0,4,2,7,1,2,14'


def parse_input(raw_input: str) -> List[int]:
    return [int(n) for n in raw_input.split(',')]


def get_fuel_consumption(crab_positions: List[int], position: int):
    return sum([abs(crab_pos - position) for crab_pos in crab_positions])


def find_optimal_position(crab_positions: List[int]) -> int:
    candidate_pos = int(sum(crab_positions) / len(crab_positions))
    candidate_fuel = get_fuel_consumption(crab_positions, candidate_pos)

    while True:
        one_up_fuel = get_fuel_consumption(crab_positions, candidate_pos + 1)
        one_down_fuel = get_fuel_consumption(crab_positions, candidate_pos - 1)
        if one_up_fuel < candidate_fuel:
            candidate_pos = candidate_pos + 1
        elif one_down_fuel < candidate_fuel:
            candidate_pos = candidate_pos - 1
        else:
            return candidate_pos
        candidate_fuel = get_fuel_consumption(crab_positions, candidate_pos)


# Test part 1
test_crab_positions = parse_input(raw_test_data)
assert find_optimal_position(test_crab_positions) == 2


if __name__ == "__main__":
    raw_input = read_input("data/day7.txt")[0]

    # Part 1
    crab_positions = parse_input(raw_input)
    optimal_position = find_optimal_position(crab_positions)
    print(f"Part 1: {get_fuel_consumption(crab_positions, optimal_position)}")
