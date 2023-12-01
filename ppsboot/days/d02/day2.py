
from functools import reduce
from ppsboot.utils.inputfile import InputFile
from ppsboot.utils.solution import Solution


class Day2(Solution):
    """ Day 2's solution.

    Problem statement is [here](https://adventofcode.com/2021/day/2).
    """

    def __init__(self):
        super().__init__(2, 'ppsboot/days/d02/input.txt')

    def load_input(self, filename: str) -> list[tuple[str, int]]:
        tuples = InputFile(filename).as_tuples()
        return list(map(lambda t: (t[0], int(t[1])), tuples))

    def calculate_position(self, position: tuple[int, int],
                           instruction: tuple[str, int]) -> tuple[int, int]:
        """ X increases by `distance`. `y` goes `up` or `down` by `distance`.
        """
        (x, y) = position
        (direction, distance) = instruction
        match direction:
            case 'forward':
                return (x + distance, y)
            case 'down':
                return (x, y + distance)  # Down increases your depth.
            case 'up':
                return (x, y - distance)

    def part1(self, input: tuple[str, int]) -> int:
        (new_x, new_y) = reduce(self.calculate_position, input, (0, 0))
        return new_x * new_y

    def calculate_position_with_aim(
        self, position: tuple[int, int, int],
        instruction: tuple[str, int]
    ) -> tuple[int, int, int]:
        """
        X increases by distance only if direction is `forward`.
        Y increases by `aim` * `distance` if direction is `forward`.
        If we're going `up` or `down`, we change our aim.
        """
        (x, y, aim) = position
        (direction, distance) = instruction
        match direction:
            case 'forward':
                return (x + distance, y + aim * distance, aim)
            case 'down':
                return (x, y, aim + distance)  # Down increases your depth.
            case 'up':
                return (x, y, aim - distance)

    def part2(self, input: list[tuple[str, int]]) -> int:
        (new_x, new_y, _) = reduce(self.calculate_position_with_aim, input, (0, 0, 0))
        return new_x * new_y
