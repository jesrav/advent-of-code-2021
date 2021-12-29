"""Slow implementation, but handles non 45 degree slopes as well"""
from dataclasses import dataclass
from typing import List

import numpy as np
from tqdm import tqdm

from common import read_input

raw_test_data = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


@dataclass
class Point:
    x: int
    y: int

    def as_np_array(self) -> np.array:
        return np.array([self.x, self.y])


@dataclass
class Line:

    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
        self.slope = self.get_slope()
        self.intersect = self.get_intersect()
        self.min_x = min(point1.x, point2.x)
        self.max_x = max(point1.x, point2.x)
        self.min_y = min(point1.y, point2.y)
        self.max_y = max(point1.y, point2.y)

    def get_slope(self):
        if self.point2.x - self.point1.x != 0:
            return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)
        else:
            return None

    def get_intersect(self):
        if self.slope is None:
            return None
        elif (self.point1.x == 0) or (self.slope == 0):
            return self.point1.y
        else:
            return self.point1.y - (self.slope * self.point1.x)

    def on_line(self, point: Point):
        if not self.min_x <= point.x <= self.max_x:
            return False
        if not self.min_y <= point.y <= self.max_y:
            return False
        if self.slope is None:
            if point.x == self.min_x:
                return True
            else:
                return False
        return point.y == self.slope * point.x + self.intersect

    def get_points(self):
        potential_points = [
            Point(x, y)
            for x in range(self.min_x, self.max_x + 1)
            for y in range(self.min_y, self.max_y + 1)
        ]
        return [p for p in potential_points if self.on_line(p)]


class Area:

    def __init__(self, size_x: int, size_y: int) -> None:
        self.grid = np.zeros((size_y, size_x))

    def add_vent(self, point):
        self.grid[point.x, point.y] += 1

    def add_vents(self, points: List[Point]):
        for p in points:
            self.add_vent(p)

    @property
    def dangerous_area_tally(self):
        return (self.grid > 1).sum()


def parse_single_line(input_line: str) -> Line:
    start_end_point_strings = input_line.split(" -> ")
    coordinate_strings = [s.split(",") for s in start_end_point_strings]
    start_end_points = [Point(int(x), int(y)) for (x, y) in coordinate_strings]
    return Line(start_end_points[0], start_end_points[1])


def parse_raw_input(raw_input: List[str]) -> List[Line]:
    parsed = []
    for raw_input_line in raw_input:
        parsed.append(parse_single_line(raw_input_line))
    return parsed

test_vent_lines = parse_raw_input(raw_test_data)
test_vent_lines_hor_vert = [l for l in test_vent_lines if l.slope is None or l.slope == 0]

# Part 1 test
test_area1 = Area(10, 10)
for line in test_vent_lines_hor_vert:
    test_area1.add_vents(line.get_points())
assert test_area1.dangerous_area_tally == 5

# Part 2 test
test_area2 = Area(10, 10)
for line in test_vent_lines:
    test_area2.add_vents(line.get_points())
assert test_area2.dangerous_area_tally == 12


if __name__ == "__main__":
    raw_input = read_input("data/day5.txt")
    vent_lines = parse_raw_input(raw_input)
    vent_lines_hor_vert = [l for l in vent_lines if l.slope is None or l.slope == 0]
    vent_lines_diag = [l for l in vent_lines if l.slope is not None and l.slope != 0]

    max_x_area = max([l.max_x for l in vent_lines]) + 1
    max_y_area = max([l.max_y for l in vent_lines]) + 1

    # Part 1
    area1 = Area(max_x_area, max_y_area)
    for line in tqdm(vent_lines_hor_vert):
        area1.add_vents(line.get_points())
    print(f"Part 1: {area1.dangerous_area_tally}")

    # Part 2
    area2 = Area(max_x_area, max_y_area)

    for line in tqdm(vent_lines):
        area2.add_vents(line.get_points())
    print(f"Part 2: {area2.dangerous_area_tally}")
