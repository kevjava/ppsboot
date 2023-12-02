from dataclasses import dataclass
from ppsboot.utils.solution import Solution


@dataclass
class Point():
    x: int
    y: int

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"


class Vector():
    """ A vector - contains a starting point and an ending point. """

    def __init__(self, start: tuple, end: tuple) -> None:
        self._start = Point(start[0], start[1])
        self._end = Point(end[0], end[1])

    @property
    def start(self) -> Point:
        """ Returns the start. """
        return self._start

    @property
    def end(self) -> Point:
        """ Returns the end. """
        return self._end

    def is_left(self) -> bool:
        """ Returns True if the vector is going left. """
        return self.start.x > self.end.x

    def is_right(self) -> bool:
        """ Returns True if the vector is going right. """
        return self.start.x < self.end.x

    def is_up(self) -> bool:
        """ Returns True if the vector is going up. """
        return self.start.y > self.end.y

    def is_down(self) -> bool:
        """ Returns True if the vector is going down. """
        return self.start.y < self.end.y

    def is_line(self) -> bool:
        """ Returns True if the vector is a line. """
        return self.start.x == self.end.x or self.start.y == self.end.y

    def distance(self) -> int:
        """ Returns the distance of the vector. """
        return max(abs(self.start.x - self.end.x), abs(self.start.y - self.end.y))

    def maxx(self) -> int:
        """ Returns the max x value. """
        return max(self.start.x, self.end.x)

    def maxy(self) -> int:
        """ Returns the max y value. """
        return max(self.start.y, self.end.y)

    def __repr__(self) -> str:
        return f"Vector: {self.start} -> {self.end}"


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
        """ Plots a vector on the grid. """
        x = vec.start.x
        y = vec.start.y
        for n in range(0, vec.distance() + 1):
            self._grid[y][x] += 1
            if (vec.is_left()):
                x -= 1
            elif (vec.is_right()):
                x += 1

            if (vec.is_up()):
                y -= 1
            elif (vec.is_down()):
                y += 1

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
        return Vector((int(startx), int(starty)), (int(endx), int(endy)))

    def load_input(self, filename: str) -> list[Vector]:
        """ Loads the input file.

        Args:
            filename (str): The name of the input file.

        Returns:
            list: The input file as a list of strings.
        """
        with open(filename) as f:
            return [self.parse_line(line) for line in f.readlines()]

    def part1(self, input: list[Vector]) -> int:
        """ Returns the solution to part 1. """
        width = max([vec.maxx() for vec in input]) + 1
        height = max([vec.maxy() for vec in input]) + 1
        grid = Grid(width, height)

        for vec in input:
            if (vec.is_line()):
                grid.plot(vec)

        return grid.count_overlaps()

    def part2(self, input: list[Vector]) -> int:
        """ Returns the solution to part 1. """
        width = max([vec.end.x for vec in input]) + 1
        height = max([vec.end.y for vec in input]) + 1
        grid = Grid(width, height)

        for vec in input:
            grid.plot(vec)

        return grid.count_overlaps()
