from dataclasses import dataclass, field
from functools import reduce
from typing_extensions import Self  # 3.10 kludge
from ppsboot.utils.solution import Solution


MatchingChars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


# [0] is the error score, [1] is the completion score
ClosingChars = {
    ')': (3, 1),
    ']': (57, 2),
    '}': (1197, 3),
    '>': (25137, 4),
}


@dataclass
class Line:
    line: str
    is_corrupted: bool = field(default=False)
    is_incomplete: bool = field(default=False)
    error: str = field(default=None)
    completion: list[str] = field(default=None)

    def error_score(self):
        """ Returns the error score. """
        return ClosingChars[self.error][0] if self.error else 0

    def completion_score(self):
        """ Returns the completion score. """
        return reduce(lambda x, y: x * 5 + y,
                      [ClosingChars[x][1] for x in self.completion]) if self.completion else 0

    def __complete_line(self, stack: list[str]) -> list[str]:
        """ Returns the completion characters for the line. """
        completion = [MatchingChars[char] for char in stack]
        completion.reverse()  # reverse() returns None, so we can't chain it
        return completion

    def parse(self) -> Self:
        """ Parses the line. Returns the `Line` for chaining. """
        stack = []
        for char in self.line:
            if char in MatchingChars:
                stack.append(char)
            elif char in ClosingChars:
                if len(stack) == 0:
                    return None
                if char == MatchingChars[stack[-1]]:
                    stack.pop()
                else:
                    self.error = char
                    self.is_corrupted = True
                    return self
            else:
                raise ValueError(f'Invalid character: {char}')
        if len(stack) > 0:
            self.is_incomplete = True
            self.completion = self.__complete_line(stack)
        return self


class Day10(Solution):
    """ Day 10 solution."""

    def __init__(self):
        super().__init__(10, 'ppsboot/days/d10/input.txt')

    def load_input(self, filename: str) -> list[list[str]]:
        with open(filename) as f:
            return [list(line.strip()) for line in f.readlines()]

    def part1(self, input: list[list[str]]) -> int:
        """ Returns the solution to part 1. """
        lines = [line.parse() for line in [Line(line) for line in input]]
        scores = [line.error_score() for line in lines if line.is_corrupted]
        return sum(scores)

    def part2(self, input: list[list[str]]) -> int:
        """ Returns the solution to part 2. """
        lines = [line.parse() for line in [Line(line) for line in input]]
        scores = sorted([line.completion_score() for line in lines if line.is_incomplete])
        return scores[len(scores)//2]
