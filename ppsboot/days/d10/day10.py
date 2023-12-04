from dataclasses import dataclass
from functools import reduce
from ppsboot.utils.solution import Solution


MatchingChars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


@dataclass(frozen=True)
class ClosingChar:
    """ Closing character. """
    char: str
    error_score: int
    completion_score: int


ClosingChars = {
    ')': ClosingChar(')', 3, 1),
    ']': ClosingChar(']', 57, 2),
    '}': ClosingChar('}', 1197, 3),
    '>': ClosingChar('>', 25137, 4),
}


class Line:
    """ Line class."""

    __line: str
    __is_corrupted = False
    __is_incomplate = False
    __error = None
    __completion = None

    @property
    def is_corrupted(self):
        """ Returns True if the line is corrupted. """
        return self.__is_corrupted

    @property
    def error(self):
        """ Returns the error character. """
        return self.__error

    @property
    def is_incomplete(self):
        """ Returns True if the line is incomplete. """
        return self.__is_incomplate

    @property
    def completion(self):
        """ Returns the completion character. """
        return self.__completion

    def error_score(self):
        """ Returns the error score. """
        return ClosingChars[self.__error].error_score if self.__error else 0

    def completion_score(self):
        """ Returns the completion score. """
        if (self.__completion):
            return reduce(lambda x, y: x * 5 + y,
                          [ClosingChars[x].completion_score for x in self.__completion])
        else:
            return 0

    def __init__(self, line: str):
        self.__line = line

    def __completion_char(self, char: str) -> str:
        """ Returns the completion character. """
        return MatchingChars[char] if char in MatchingChars else None

    def __complete_line(self, stack: list[str]) -> list[str]:
        """ Returns the completion characters for the line. """
        completion = [self.__completion_char(char) for char in stack]
        completion.reverse()  # reverse() returns None, so we can't chain it
        return completion

    def parse(self):
        """ Parses the line. """
        stack = []
        for char in self.__line:
            if char in MatchingChars:
                stack.append(char)
            elif char in ClosingChars:
                if len(stack) == 0:
                    return None
                if char == MatchingChars[stack[-1]]:
                    stack.pop()
                else:
                    self.__error = char
                    self.__is_corrupted = True
                    return
            else:
                pass  # print("WTF:", char)
        if len(stack) > 0:
            self.__is_incomplate = True
            self.__completion = self.__complete_line(stack)

    def __repr__(self):
        return (f"Line({self.__line}, "
                f"corrupted: {self.__is_corrupted}, "
                f"incomplete: {self.__is_incomplate}, "
                f"error: {self.__error}, "
                f"error score: {self.error_score()}, "
                f"completion: {self.__completion}, "
                f"completion score: {self.completion_score()}")


class Day10(Solution):
    """ Day 10 solution."""

    def __init__(self):
        super().__init__(10, 'ppsboot/days/d10/input.txt')

    def load_input(self, filename: str) -> list[list[str]]:
        with open(filename) as f:
            return [list(line.strip()) for line in f.readlines()]

    def parse_line(self, line: str) -> str | None:
        """ Parses a line of input. """

    def part1(self, input: list[list[str]]) -> int:
        """ Returns the solution to part 1. """
        lines = [Line(line) for line in input]
        [line.parse() for line in lines]
        [print(line) for line in lines]
        scores = [line.error_score() for line in lines if line.is_corrupted]
        print(scores)
        return sum(scores)

    def part2(self, input: list[list[str]]) -> int:
        """ Returns the solution to part 2. """
        lines = [Line(line) for line in input]
        [line.parse() for line in lines]
        [print(line) for line in lines]
        scores = sorted([line.completion_score() for line in lines if line.is_incomplete])
        print(scores)
        return scores[len(scores)//2]
