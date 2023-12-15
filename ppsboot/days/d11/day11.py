from dataclasses import dataclass
from ppsboot.utils.solution import Solution


@dataclass
class OctopusGrid:
    """ A grid of octopuses, each with an energy level. """

    rows: list[list[int]]

    def __repr__(self) -> str:
        return '\n'.join([''.join([str(n) if n < 10 else '*' for n in row]) for row in self.rows])

    def __get_adjacents(self, this_x: int, this_y: int) -> list[tuple[int, int]]:
        """ Get adjacent cells, returning a list of coordinates.

        Uses `max` and `min` to avoid out-of-bounds errors.
        """
        return [(x, y)
                for y in range(max(0, this_y-1), min(len(self.rows), this_y+2))
                for x in range(max(0, this_x-1), min(len(self.rows[y]), this_x+2))
                if not (x == this_x and y == this_y)]

    def __flash(self, this_x: int, this_y: int) -> None:
        """ Flash the octopus at the given coordinates. Give all the adjacent octopuses a point of
        energy."""
        for (x, y) in self.__get_adjacents(this_x, this_y):
            if (self.rows[y][x] > 0):  # This guy just flashed if he's at zero.
                self.rows[y][x] += 1
        self.rows[this_y][this_x] = 0

    def step(self) -> int:
        """ Performs a single step.

        Energy level increases by 1 for everybody, and then we flash any octopus with energy > 9,
        until they're all done flashing. Returns the number of flashes that happened in this step.
        """
        flashes = 0

        self.rows = [[n + 1 for n in row] for row in self.rows]

        # While there are any octopuses with energy > 9, flash them.
        while any([any([n > 9 for n in row]) for row in self.rows]):
            for (x, y) in [(x, y) for x in range(len(self.rows))
                           for y in range(len(self.rows[x]))
                           if self.rows[y][x] > 9]:
                self.__flash(x, y)
                flashes += 1

        return flashes


class Day11(Solution):

    def __init__(self):
        super().__init__(11, 'ppsboot/days/d11/input.txt')

    def load_input(self, filename: str) -> OctopusGrid:
        with open(self._filename) as f:
            chars = [list(line.strip()) for line in f.readlines()]
            return OctopusGrid([[int(char) for char in row] for row in chars])

    def part1(self, grid: OctopusGrid) -> int:
        """ Find the number of flashes in 100 steps. """
        total_steps = 100
        flashes = 0
        for x in range(total_steps):
            flashes += grid.step()
        return flashes

    def part2(self, grid: OctopusGrid) -> int:
        """ Find the first step where all octopuses flash. """
        step = 0
        while True:
            step += 1
            flashes = grid.step()
            if flashes == (len(grid.rows) * len(grid.rows[0])):
                return step
