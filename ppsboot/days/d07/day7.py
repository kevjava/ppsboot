from ppsboot.utils.solution import Solution


class Day7(Solution):
    """ Day 7 solution.

    The Treachery of Whales

    https://adventofcode.com/2021/day/7
    """

    def __init__(self):
        super().__init__(7, 'ppsboot/days/d07/input.txt')

    def load_input(self, filename: str) -> list[str]:
        with open(filename) as f:
            return [int(x) for x in f.readline().split(',')]

    def part1(self, input: list[str]) -> int:
        """ Returns the solution to part 1. """
        distance = [0 for x in range(max(input)+1)]
        for i in range(max(input)+1):
            thisdistance = [abs(i - x) for x in input]
            distance[i] = sum(thisdistance)

        return min(distance)

    def part2(self, input: list[str]) -> int:
        """ Returns the solution to part 2. """
        costs = [0 for x in range(max(input)+1)]
        for i in range(1, max(input)+1):
            costs[i] = costs[i-1] + i

        distances = [0 for x in range(max(input)+1)]
        for i in range(max(input)+1):
            thisdistance = [costs[abs(i - x)] for x in input]
            distances[i] = sum(thisdistance)

        return min(distances)
