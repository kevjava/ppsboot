from dataclasses import dataclass
import re
import typing
from ppsboot.utils.solution import Solution


Point = typing.NamedTuple("Point", [('x', int), ('y', int)])
Fold = typing.NamedTuple("Fold", [('axis', str), ('point', int)])


@dataclass
class OrigamiPage:
    """ Represents an origami page. """
    points: set[Point]
    instructions: list[str]

    def __str__(self):
        max_x = max([point.x for point in self.points])
        max_y = max([point.y for point in self.points])
        return '\n'.join([''.join(['#' if Point(x, y) in self.points else '.'
                                   for x in range(max_x + 1)])
                          for y in range(max_y + 1)])


class Day13(Solution):

    def __init__(self):
        super().__init__(13, 'ppsboot/days/d13/input.txt')

    _fold_pattern = re.compile(r"([xy])=(\d+)")

    def parse_point(self, line):
        (x, y) = line.split(",")
        return Point(int(x), int(y))

    def parse_fold(self, line):
        """ Parses a fold. """
        matches = self._fold_pattern.search(line)
        return Fold(matches.group(1), int(matches.group(2)))

    def load_input(self, filename: str) -> OrigamiPage:
        """ Loads the input. """
        with open(filename) as f:
            (board, instructions) = "".join(f.readlines()).split("\n\n")
            points = set([self.parse_point(point) for point in board.split("\n")])
            folds = [self.parse_fold(fold) for fold in instructions.split("\n")]
            return OrigamiPage(points, folds)

    # def fold(self, points: list[Point], fold: Fold) -> set[Point]:
    def fold(self, page: OrigamiPage) -> OrigamiPage:
        fold = page.instructions[0]
        new_points: set[Point] = set()
        if fold.axis == "x":
            for point in page.points:
                if point.x < fold.point:
                    new_points.add(Point(point.x, point.y))
                elif point.x > fold.point:
                    # Mirror around the fold point.
                    new_x = fold.point - (point.x - fold.point)
                    new_points.add(Point(new_x, point.y))
        else:  # fold.axis == "y"
            for point in page.points:
                if point.y < fold.point:
                    new_points.add(Point(point.x, point.y))
                elif point.y > fold.point:
                    # Mirror around the fold point.
                    new_y = fold.point - (point.y - fold.point)  # 7 - (9 - 7) = 5
                    new_points.add(Point(point.x, new_y))
                else:
                    pass  # Remove the point.
        return OrigamiPage(new_points, page.instructions[1:])

    def part1(self, page: OrigamiPage) -> int:
        """ Returns the solution to part 1. """
        page = self.fold(page)
        return len(page.points)

    def part2(self, page: OrigamiPage) -> int:
        """ Returns the solution to part 2. """
        while (page.instructions):
            page = self.fold(page)

        return (f"\n{str(page)}")
