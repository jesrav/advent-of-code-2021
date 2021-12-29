from typing import List


test_data = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


def read_input(fpath: str) -> List[str]:
    with open(fpath) as f:
        return [int(line.replace('\n', '')) for line in f.readlines()]


def count_increasing_depths(depths: List[int]) -> int:
    count = 0
    for i, depth in enumerate(depths[1:], start=1):
        previous_depth = depths[i - 1]
        if depth > previous_depth:
            count += 1
    return count    


def create_moving_averages(depths: List[int]) -> List[int]:
    moving_sums = []
    for i, depth in enumerate(depths):
        if i < 2:
            moving_sum = None
        else:
            moving_sum = depth + depths[i - 1] + depths[i - 2]
        moving_sums.append(moving_sum)
    return moving_sums


assert count_increasing_depths(test_data) == 7
assert count_increasing_depths(create_moving_averages(test_data)[2:]) == 5

if __name__ == "__main__":
    input_data = read_input("data/day1.txt")  
    print(f"Part 1: {count_increasing_depths(input_data)}")  

    part2 = count_increasing_depths(create_moving_averages(input_data)[2:])
    print(f"Part 2: {part2}")
