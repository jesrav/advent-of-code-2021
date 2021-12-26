from dataclasses import dataclass
from typing import List


test_data = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def read_input(fpath: str) -> List[str]:
    with open(fpath) as f:
        return [line.replace('\n', '') for line in f.readlines()]
        

@dataclass
class SubmarineStep:
    horizontal_step: int
    depth_step: int


def parse_course_input(input_list: List[str]) -> List[SubmarineStep]:
    directions=  [s.split(" ") for s in input_list]
    submarine_steps = []
    for direction in directions:
        if direction[0] == "forward":
            submarine_step = SubmarineStep(int(direction[1]), 0)
        elif direction[0] == "up":
            submarine_step = SubmarineStep(0, -int(direction[1]))    
        elif direction[0] == "down":
            submarine_step = SubmarineStep(0, int(direction[1]))    
        else:
            raise ValueError(f"direction {direction[0]} not valid. Must be up, down or forward.")
        submarine_steps.append(submarine_step)
    return submarine_steps


class Submarine:

    def __init__(self, start_horizontal: int, start_depth: int):
        self.horizontal_position = start_horizontal
        self.depth_position = start_depth

    def change_depth(self, step: int):
        self.horizontal_position += step 
    
    def change_horizontal(self, step: int):
        self.depth_position += step 

    @property
    def position(self):
        return self.horizontal_position, self.depth_position

    def sail_planned_course(self, planned_course: List[SubmarineStep]):
        for submarine_step in planned_course:
            self.change_horizontal(submarine_step.horizontal_step)
            self.change_depth(submarine_step.depth_step)


# Test case part 1
submarine = Submarine(0, 0)
submarine.sail_planned_course(parse_course_input(test_data))
assert submarine.position[0] * submarine.position[1] == 150


if __name__ == "__main__":
    input_data = read_input("data/day2.txt")
    submarine = Submarine(0, 0)
    submarine.sail_planned_course(parse_course_input(input_data))
    part1 = submarine.position[0] * submarine.position[1]
    print(f"Part 1: {part1} ") 