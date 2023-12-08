from dataclasses import dataclass
from ppsboot.utils.solution import Solution


@dataclass
class Display:
    signal_patterns: list[str]
    outputs: list[str]

    @property
    def signal_patterns(self) -> list[str]:
        return self._signal_patterns

    @property
    def outputs(self) -> list[str]:
        return self._outputs

    def __init__(self, line: str) -> None:
        (signal_patterns_str, outputs_str) = line.split(' | ')
        self._signal_patterns = list(signal_patterns_str.split(' '))
        self._outputs = list(outputs_str.split(' '))

    def __repr__(self) -> str:
        return f"Display({self._signal_patterns}, {self._outputs})"

    def decode(self) -> int:
        """ Returns the decoded four-digit number. """
        self._outputs = [''.join(list(sorted(output))) for output in self._outputs]
        self._signal_patterns = [''.join(list(sorted(pattern)))
                                 for pattern in self._signal_patterns]

        codex: dict[str, str] = {}
        one_coded = [pattern for pattern in self._signal_patterns
                     if len(pattern) == 2][0]
        codex[one_coded] = '1'  # The only one with two segments lit.

        seven_coded = [pattern for pattern in self._signal_patterns
                       if len(pattern) == 3][0]
        codex[seven_coded] = '7'  # The only one with three segments lit.

        four_coded = [pattern for pattern in self._signal_patterns
                      if len(pattern) == 4][0]
        codex[four_coded] = '4'  # The only one with four segments lit.

        eight_coded = [pattern for pattern in self._signal_patterns
                       if len(pattern) == 7][0]
        codex[eight_coded] = '8'  # The only one with seven segments lit.

        nine_coded = [pattern for pattern in self._signal_patterns
                      if len(pattern) == 6
                      and set(four_coded).issubset(set(pattern))][0]
        codex[nine_coded] = '9'  # Six segments lit, and it contains all the segments of the four.

        zero_coded = [pattern for pattern in self._signal_patterns
                      if len(pattern) == 6
                      and set(seven_coded).issubset(set(pattern))
                      and not set(four_coded).issubset(set(pattern))][0]
        codex[zero_coded] = '0'  # Six segments lit, and it contains all the segments of the seven.

        six_coded = [pattern for pattern in self._signal_patterns
                     if len(pattern) == 6
                     and pattern is not nine_coded
                     and pattern is not zero_coded][0]
        codex[six_coded] = '6'  # Six segments lit, and it isn't the nine or the zero. :)

        two_coded = [pattern for pattern in self._signal_patterns
                     if len(pattern) == 5 and not set(pattern).issubset(set(nine_coded))][0]
        codex[two_coded] = '2'  # Five segments lit and the nine doesn't contain it.

        five_coded = [pattern for pattern in self._signal_patterns
                      if len(pattern) == 5 and set(pattern).issubset(set(six_coded))][0]
        codex[five_coded] = '5'  # Five segments lit, and it is contained in the six.

        three_coded = [pattern for pattern in self._signal_patterns
                       if len(pattern) == 5
                       and pattern is not five_coded
                       and pattern is not two_coded][0]
        codex[three_coded] = '3'  # Five segments lit, and it isn't the five or the two.

        ret_str = ''
        for output in self._outputs:
            ret_str += (codex[output])
        return int(ret_str)


class Day8(Solution):
    """ Day 8 solution."""

    def __init__(self) -> None:
        super().__init__(8, 'ppsboot/days/d08/input.txt')

    def load_input(self, filename: str) -> list[Display]:
        with open(filename) as f:
            return [Display(line.strip()) for line in f.readlines()]

    def part1(self, displays: list[Display]) -> int:
        """ Returns the solution to part 1. """
        outputs = [display.outputs for display in displays]
        uniques = len([character for characters in outputs for character in characters
                      if len(character) in [2, 3, 4, 7]])
        return uniques

    def part2(self, displays: list[Display]) -> int:
        outputs: list[int] = [display.decode() for display in displays]
        return sum(outputs)
