from ppsboot.utils.solution import Solution


class Grid():
    """ Grid class. """

    def __init__(self, numbers: list[int, 2]):
        self._grid = numbers

    def __repr__(self) -> str:
        return f"Grid({self._grid})"

    def calculate_risk(self, x: int, y: int) -> int:
        """ Returns the risk level for the given coordinates. """

        def get_top():
            return self._grid[y-1][x] if y > 0 else 10

        def get_bottom():
            return self._grid[y+1][x] if y < len(self._grid)-1 else 10

        def get_left():
            return self._grid[y][x-1] if x > 0 else 10

        def is_right():
            return self._grid[y][x+1] if x < len(self._grid[y])-1 else 10

        risk = self._grid[y][x] + 1
        return risk if risk <= min(get_top(), get_bottom(), get_left(), is_right()) else 0

    def get_adjacents(self, x: int, y: int) -> list[tuple[int, 2]]:
        """ Returns a list of adjacent coordinates. """
        adjacents = []
        if y > 0:
            adjacents.append((x, y-1))
        if y < len(self._grid)-1:
            adjacents.append((x, y+1))
        if x > 0:
            adjacents.append((x-1, y))
        if x < len(self._grid[y])-1:
            adjacents.append((x+1, y))
        return adjacents

    def __getitem__(self, key: tuple[int, 2]) -> int:
        """ Returns the value at the given coordinates. """
        (x, y) = key
        return self._grid[y][x]


class Day9(Solution):
    """ Day 9 solution.

    Smoke Basin

    https://adventofcode.com/2021/day/9
    """

    def __init__(self):
        super().__init__(9, 'ppsboot/days/d09/input.txt')

    def load_input(self, filename: str) -> list[int, 2]:
        """ Returns the input file as a list of lists of characters. """
        with open(self._filename) as f:
            chars = [list(line.strip()) for line in f.readlines()]
            return [[int(char) for char in row] for row in chars]

    def part1(self, input: list[int, 2]) -> int:
        """ Returns the solution to part 1. """
        grid = Grid(input)
        risks = [[grid.calculate_risk(x, y) for x in range(len(input[y]))]
                 for y in range(len(input))]
        return sum(risks[y][x] for y in range(len(risks)) for x in range(len(risks[y])))

    def _calculate_basin_size(self, low_point: tuple[int, 2], grid: Grid) -> int:
        """ Returns the size of the basin at the given low point. """
        (x, y) = low_point
        basin = [(x, y)]
        to_check = {(x, y)}

        while len(to_check) > 0:
            (x, y) = to_check.pop()
            adjacents = grid.get_adjacents(x, y)
            for adjacent in adjacents:
                (x, y) = adjacent
                if adjacent not in basin and grid[x, y] < 9:
                    basin.append(adjacent)
                    to_check.add(adjacent)

        return len(basin)

    def part2(self, input: list[int, 2]) -> int:
        """ Returns the solution to part 2. """
        grid = Grid(input)
        risks = [[grid.calculate_risk(x, y) for x in range(len(input[y]))]
                 for y in range(len(input))]
        low_points = [(x, y) for y in range(len(risks))
                      for x in range(len(risks[y])) if risks[y][x] > 0]
        basin_sizes = [self._calculate_basin_size(low_point, grid) for low_point in low_points]
        largest_basins = sorted(basin_sizes, reverse=True)[:3]
        return largest_basins[0] * largest_basins[1] * largest_basins[2]
