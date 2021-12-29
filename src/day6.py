from typing import List

from common import read_input

test_data = "3,4,3,1,2"


class Fish:
    def __init__(self, timer: int = 8):
        self.timer = timer

    def reset_timer(self, value: int = 6):
        self.timer = value

    def age_a_day(self):
        self.timer -= 1

    def __repr__(self):
        return f"Fish(timer={self.timer})"


class FishPopulation:
    def __init__(self, fish_population: List[Fish]):
        self.fish_population = fish_population

    def increment_day(self):
        new_fish = []
        for fish in self.fish_population:
            if fish.timer == 0:
                fish.reset_timer()
                new_fish.append(Fish())
            else:
                fish.age_a_day()
        self.fish_population += new_fish

    def increment_days(self, days: int):
        for _ in range(days):
            self.increment_day()

    @property
    def size(self):
        return len(self.fish_population)

    @classmethod
    def from_raw_data(cls, raw_data: str) -> 'FishPopulation':
        fish_population = [Fish(timer=int(n)) for n in raw_data.split(",")]
        return FishPopulation(fish_population)


# Test part 1
population = FishPopulation.from_raw_data(test_data)
population.increment_days(80)
assert population.size == 5934


if __name__ == "__main__":
    raw_input = read_input("data/day6.txt")[0]
    population = FishPopulation.from_raw_data(raw_input)
    population.increment_days(80)
    print(f"Part 1: {population.size}")

