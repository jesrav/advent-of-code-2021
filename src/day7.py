from typing import List, Callable

from common import read_input

raw_test_data = '16,1,2,0,4,2,7,1,2,14'


def parse_input(raw_input: str) -> List[int]:
    return [int(n) for n in raw_input.split(',')]


def part1_fuel_consumption(distance) -> int:
    return distance


def part2_fuel_consumption(distance) -> int:
    return int(distance * (distance + 1) / 2)


def get_fuel_consumption(
        crab_positions: List[int], position: int, distance_func: Callable
) -> int:
    distances = [abs(crab_pos - position) for crab_pos in crab_positions]
    return sum([distance_func(dist) for dist in distances])


def find_optimal_position(crab_positions: List[int], distance_func: Callable) -> int:
    candidate_pos = int(sum(crab_positions) / len(crab_positions))
    candidate_fuel = get_fuel_consumption(crab_positions, candidate_pos, distance_func)

    while True:
        one_up_fuel = get_fuel_consumption(crab_positions, candidate_pos + 1, distance_func)
        one_down_fuel = get_fuel_consumption(crab_positions, candidate_pos - 1, distance_func)
        if one_up_fuel < candidate_fuel:
            candidate_pos = candidate_pos + 1
        elif one_down_fuel < candidate_fuel:
            candidate_pos = candidate_pos - 1
        else:
            return candidate_pos
        candidate_fuel = get_fuel_consumption(crab_positions, candidate_pos, distance_func)


# Test part 1
test_crab_positions = parse_input(raw_test_data)
assert find_optimal_position(test_crab_positions, part1_fuel_consumption) == 2

# Test part 2
assert find_optimal_position(test_crab_positions, part2_fuel_consumption) == 5


if __name__ == "__main__":
    raw_input = read_input("data/day7.txt")[0]
    crab_positions = parse_input(raw_input)

    # Part 1
    optimal_position = find_optimal_position(crab_positions, part1_fuel_consumption)
    print(f"Part 1: {get_fuel_consumption(crab_positions, optimal_position, part1_fuel_consumption)}")

    # Part 2
    optimal_position = find_optimal_position(crab_positions, part2_fuel_consumption)
    print(f"Part 1: {get_fuel_consumption(crab_positions, optimal_position, part2_fuel_consumption)}")