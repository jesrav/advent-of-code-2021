from collections import Counter, defaultdict
from typing import Dict

from common import read_input

test_data = "3,4,3,1,2"


# class FishCohort:
#     def __init__(self, timer: int = 8, fish_tally: int = 1):
#         self.timer = timer
#         self.fish_tally = fish_tally
#
#     def add_fish(self, n):
#         self.fish_tally += n
#
#     def reset_timer(self, value: int = 6):
#         self.timer = value
#
#     def age_a_day(self):
#         self.timer -= 1
#
#     def __repr__(self):
#         return f"Fish(timer={self.timer})"
#
#
# class FishPopulation:
#     def __init__(self, fish_population: List[FishCohort]):
#         self.fish_population = fish_population
#
#     def add_new_fish(self, n: int):
#         [f for f in self.fish_population if f.timer == timer][0]
#
#     def increment_day(self):
#         new_fish = []
#         for cohort in self.fish_population:
#             if cohort.timer == 0:
#                 cohort.reset_timer()
#
#             else:
#                 cohort.age_a_day()
#         self.fish_population += new_fish
#
#     def increment_days(self, days: int):
#         for _ in range(days):
#             self.increment_day()
#
#     @property
#     def size(self):
#         return len(self.fish_population)
#
#     @classmethod
#     def from_raw_data(cls, raw_data: str) -> 'FishPopulation':
#         fish_population = [Fish(timer=int(n)) for n in raw_data.split(",")]
#         return FishPopulation(fish_population)


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
