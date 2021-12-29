from dataclasses import dataclass
from typing import List

from common import read_input

test_data = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]
        

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

    def __init__(self, start_horizontal: int, start_depth: int, use_aim: bool = False, start_aim: int = 0):
        self.horizontal_position = start_horizontal
        self.depth_position = start_depth
        self.use_aim = use_aim
        self.aim = start_aim

    def change_depth(self, step: SubmarineStep):
        self.horizontal_position += step.horizontal_step
    
    def change_horizontal(self, step: SubmarineStep):
        if self.use_aim:
            self.depth_position += self.aim*step.horizontal_step
        else:
            self.depth_position += step.depth_step

    def update_aim(self, step: SubmarineStep):
        self.aim += step.depth_step

    @property
    def position(self):
        return self.horizontal_position, self.depth_position

    def sail_planned_course(self, planned_course: List[SubmarineStep]):
        for submarine_step in planned_course:
            self.change_horizontal(submarine_step)
            self.change_depth(submarine_step)
            self.update_aim(submarine_step)

# Test case part 1
submarine = Submarine(0, 0)
submarine.sail_planned_course(parse_course_input(test_data))
assert submarine.position[0] * submarine.position[1] == 150

# Test case part 2
submarine = Submarine(0, 0, use_aim=True)
submarine.sail_planned_course(parse_course_input(test_data))
assert submarine.position[0] * submarine.position[1] == 900

if __name__ == "__main__":
    input_data = read_input("data/day2.txt")

    # Part 1
    submarine = Submarine(0, 0)
    submarine.sail_planned_course(parse_course_input(input_data))
    part1 = submarine.position[0] * submarine.position[1]
    print(f"Part 1: {part1} ") 

    # Part 2
    submarine = Submarine(0, 0, use_aim=True)
    submarine.sail_planned_course(parse_course_input(input_data))
    part1 = submarine.position[0] * submarine.position[1]
    print(f"Part 2: {part1} ") 