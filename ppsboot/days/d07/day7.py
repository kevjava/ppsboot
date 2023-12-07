import itertools
from ppsboot.utils.solution import Solution


class Day7(Solution):
    """ Day 7 solution.

    The Treachery of Whales

    https://adventofcode.com/2021/day/7
    """

    def __init__(self):
        super().__init__(7, 'ppsboot/days/d07/input.txt')

    def load_input(self, filename: str) -> list[int]:
        with open(filename) as f:
            return [int(x) for x in f.readline().split(',')]

    def part1(self, input: list[int]) -> int:
        """ Returns the solution to part 1. """
        distance = [0 for x in range(max(input)+1)]
        for i in range(max(input)+1):
            thisdistance = [abs(i - x) for x in input]
            distance[i] = sum(thisdistance)

        return min(distance)

    def part2(self, input: list[int]) -> int:
        """ Returns the solution to part 2. """
        costs = list(itertools.accumulate(range(max(input)+1)))

        distances = [0 for x in range(max(input)+1)]
        for i in range(max(input)+1):
            thisdistance = [costs[abs(i - x)] for x in input]
            distances[i] = sum(thisdistance)

        return min(distances)
