from ppsboot.utils.solution import Solution


class Day6(Solution):
    """ Day 6 solution.

    https://adventofcode.com/2021/day/6
    """

    def __init__(self):
        super().__init__(6, 'ppsboot/days/d06/input.txt')

    def load_input(self, filename: str) -> list[int]:
        with open(filename) as f:
            return [int(x) for x in f.readline().split(',')]

    def next_state(self, input: list[int]) -> list[int]:
        """ Returns the next state. """
        to_create = input.count(0)
        new_state = [x-1 if x > 0 else 6 for x in input]
        for i in range(to_create):
            new_state.append(8)
        return new_state

    def next_state_but_smart(self, counts: list[int]) -> list[int]:
        """ Returns the next state. """
        to_create = counts[0]
        new_state = list(counts)
        to_create = new_state.pop(0)
        new_state[6] += to_create
        new_state.append(to_create)
        return new_state

    def part1(self, input: list[str]) -> int:
        """ Returns the solution to part 1. """
        end = 80
        for day in range(1, end + 1):
            input = self.next_state(input)
            # print(f"After {day} day", len(input))

        return len(input)

    def part2(self, input: list[str]) -> int:
        """ Returns the solution to part 2. """
        counts = [list.count(input, x) for x in range(0, 9)]
        end = 256
        for day in range(1, end + 1):
            counts = self.next_state_but_smart(counts)
            # print(f"After {day} day", counts)
        return sum(counts)
