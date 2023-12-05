from dataclasses import dataclass, field
from ppsboot.utils.solution import Solution


@dataclass(frozen=True)
class Point():
    """ A point on the grid. Yeah, this could be a tuple, but I like being able to name the
    fields."""
    x: int = field()
    y: int = field()


@dataclass(frozen=True)
class Vector():
    """ A vector - contains a starting point, an ending point, and a lot of convenience methods. """
    start: Point = field()
    end: Point = field()


class Grid():
    """ Represents an (x,y) grid. """

    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        self._grid = [[0 for x in range(width+1)] for y in range(height)]

    def __repr__(self) -> str:
        ret = ''
        for row in self._grid:
            ret += f"{row}\n"
        return ret

    def plot(self, vec: Vector) -> None:
        """ Plots a vector on the grid.
        """
        x = vec.start.x
        y = vec.start.y

        dx = 0  # 1 means we go right, -1 means we go left
        if (vec.start.x != vec.end.x):
            dx = (vec.end.x - vec.start.x) // abs(vec.end.x - vec.start.x)

        dy = 0  # 1 means we go down, -1 means we go up
        if (vec.start.y != vec.end.y):
            dy = (vec.end.y - vec.start.y) // abs(vec.end.y - vec.start.y)

        distance = max(abs(vec.start.x - vec.end.x), abs(vec.start.y - vec.end.y))
        for n in range(0, distance + 1):
            self._grid[y][x] += 1
            x += dx
            y += dy

    def rows(self) -> list[list[int]]:
        """ Returns the rows of the grid. """
        return self._grid

    def count_overlaps(self) -> int:
        """ Counts the number of overlaps in the grid. """
        return sum([sum([1 for value in row if value > 1]) for row in self._grid])


class Day5(Solution):
    """ Day 5: Hydrothermal Venture

    https://adventofcode.com/2021/day/5
    """

    def __init__(self):
        super().__init__(5, 'ppsboot/days/d05/input.txt')

    def parse_line(self, line: str) -> Vector:
        """ Parses a line from the input file. """
        (ins_start, ins_end) = line.split(' -> ')
        (startx, starty) = ins_start.split(',')
        (endx, endy) = ins_end.split(',')
        return Vector(Point(int(startx), int(starty)), Point(int(endx), int(endy)))

    def load_input(self, filename: str) -> list[Vector]:
        with open(filename) as f:
            return [self.parse_line(line) for line in f.readlines()]

    def part1(self, input: list[Vector]) -> int:
        """ Returns the solution to part 1. """
        width = max([max(vec.start.x, vec.end.x) for vec in input]) + 1
        height = max([max(vec.start.y, vec.end.y) for vec in input]) + 1
        grid = Grid(width, height)

        for vec in input:
            if (vec.start.x == vec.end.x or vec.start.y == vec.end.y):  # Not diagonal.
                grid.plot(vec)

        return grid.count_overlaps()

    def part2(self, input: list[Vector]) -> int:
        """ Returns the solution to part 1. """
        width = max([max(vec.start.x, vec.end.x) for vec in input]) + 1
        height = max([max(vec.start.y, vec.end.y) for vec in input]) + 1
        grid = Grid(width, height)

        for vec in input:
            grid.plot(vec)

        return grid.count_overlaps()
