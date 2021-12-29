from collections import Counter, defaultdict
from typing import Dict

from common import read_input

test_data = "3,4,3,1,2"


class FishPopulation:
    def __init__(self, cohorts: Dict[int, int]):
        self.cohorts = defaultdict(lambda: 0)
        self.cohorts.update(cohorts)

    def update_cohorts(self):
        new_cohorts = {}
        new_cohorts[8] = self.cohorts[0]
        new_cohorts[7] = self.cohorts[8]
        new_cohorts[6] = self.cohorts[0] + self.cohorts[7]
        new_cohorts[5] = self.cohorts[6]
        new_cohorts[4] = self.cohorts[5]
        new_cohorts[3] = self.cohorts[4]
        new_cohorts[2] = self.cohorts[3]
        new_cohorts[1] = self.cohorts[2]
        new_cohorts[0] = self.cohorts[1]
        self.cohorts.update(new_cohorts)

    def increment_days(self, days: int):
        for _ in range(days):
            self.update_cohorts()

    @property
    def size(self):
        return sum(self.cohorts.values())

    def __repr__(self):
        return f"[{self.cohorts}]"

    @classmethod
    def from_raw_data(cls, raw_data: str) -> 'FishPopulation':
        cohorts = dict(Counter([int(n) for n in raw_data.split(",")]))
        return FishPopulation(cohorts=cohorts)


# Test part 1
population = FishPopulation.from_raw_data(test_data)
population.increment_days(80)
assert population.size == 5934

# Test part 2
population = FishPopulation.from_raw_data(test_data)
population.increment_days(256)
assert population.size == 26984457539

if __name__ == "__main__":
    raw_input = read_input("data/day6.txt")[0]

    # Part 1
    population = FishPopulation.from_raw_data(raw_input)
    population.increment_days(80)
    print(f"Part 1: {population.size}")

    # Part 2
    population = FishPopulation.from_raw_data(raw_input)
    population.increment_days(256)
    print(f"Part 2: {population.size}")
