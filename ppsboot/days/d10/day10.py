from functools import reduce
from ppsboot.utils.solution import Solution


ErrorScores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


CompletionScores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


class Line:
    """ Line class."""

    _line: str
    _is_corrupted = False
    _is_incomplate = False
    _error = None
    _completion = None

    @property
    def is_corrupted(self):
        """ Returns True if the line is corrupted. """
        return self._is_corrupted

    @property
    def error(self):
        """ Returns the error character. """
        return self._error

    @property
    def is_incomplete(self):
        """ Returns True if the line is incomplete. """
        return self._is_incomplate

    @property
    def completion(self):
        """ Returns the completion character. """
        return self._completion

    def error_score(self):
        """ Returns the error score. """
        return ErrorScores[self._error] if self._error else 0

    def completion_score(self):
        """ Returns the completion score. """
        if (self._completion):
            return reduce(lambda x, y: x * 5 + y, [CompletionScores[x] for x in self._completion])
        else:
            return 0

    def __init__(self, line: str):
        self._line = line

    def _completion_char(self, char: str) -> str:
        """ Returns the completion character. """
        if char == '[':
            return ']'
        elif char == '(':
            return ')'
        elif char == '<':
            return '>'
        elif char == '{':
            return '}'
        else:
            return None

    def _complete_line(self, stack: list[str]) -> list[str]:
        """ Returns the completion characters for the line. """
        completion = [self._completion_char(char) for char in stack]
        completion.reverse()  # reverse() returns None, so we can't chain it
        return completion

    def parse(self):
        """ Parses the line. """
        stack = []
        for char in self._line:
            if char in ['[', '(', '<', '{']:
                stack.append(char)
            elif char in [']', ')', '>', '}']:
                if len(stack) == 0:
                    return None
                if stack[-1] == '[' and char == ']':
                    stack.pop()
                elif stack[-1] == '(' and char == ')':
                    stack.pop()
                elif stack[-1] == '<' and char == '>':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                else:
                    self._error = char
                    self._is_corrupted = True
                    return
            else:
                pass  # print("WTF:", char)
        if len(stack) > 0:
            self._is_incomplate = True
            self._completion = self._complete_line(stack)

    def __repr__(self):
        return (f"Line({self._line}, "
                f"corrupted: {self._is_corrupted}, "
                f"incomplete: {self._is_incomplate}, "
                f"error: {self._error}, "
                f"error score: {self.error_score()}, "
                f"completion: {self._completion}, "
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
