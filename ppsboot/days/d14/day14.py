import collections
import itertools
import typing
from ppsboot.utils.solution import Solution


InsertionRule = typing.NamedTuple("InsertionRule", [('pattern', str), ('ins', int)])


def sliding_window(iterable, n) -> tuple:
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n-1), maxlen=n)
    for x in it:
        window.append(x)
        yield tuple(window)


class Day14(Solution):

    def __init__(self):
        super().__init__(14, 'ppsboot/days/d14/input.txt')

    def load_input(self, filename: str) -> tuple[str, dict[str, str]]:
        """ Loads the input. """
        with open(filename) as f:
            (polymer_template, insertion_rules) = "".join(f.readlines()).split("\n\n")
            rules_list = [InsertionRule(*rule.split(" -> "))
                          for rule in insertion_rules.split("\n")]
            rules = {}
            for rule in rules_list:
                rules[rule.pattern] = rule.ins

        return (polymer_template, rules)

    def build(self, polymer: str, rules: dict[str, str]) -> str:
        """ Builds the polymer. """
        new_polymer = ''
        for (a, b) in sliding_window(polymer, 2):
            new_polymer += a + rules[a + b]
        return new_polymer + polymer[-1]

    def part1(self, input: tuple[str, list[InsertionRule]]) -> int:
        """ Returns the solution to part 1. """
        (polymer, rules) = input
        print(f"Pattern: {polymer}")
        for step in range(0, 10):
            polymer = self.build(polymer, rules)
            counter = collections.Counter(polymer)
            # pair_counter = collections.Counter(a + b for (a, b) in sliding_window(polymer, 2))
            # print(f"After step {step+1}:")
            # print(polymer)
            # print(counter)
            # print(pair_counter)

        return counter.most_common()[0][1] - counter.most_common()[-1][1]

    def build_by_counts(self, freq_count: dict[str, str], rules: dict[str, str]) -> str:
        """ Builds the polymer, using counts instead of strings. """
        new_freq_count = collections.defaultdict(int)
        for pair in rules.keys():
            pair_count = freq_count[pair]
            insert_char = rules[pair]
            new_freq_count[pair[0] + insert_char] += pair_count
            new_freq_count[insert_char + pair[1]] += pair_count
        return new_freq_count

    def part2(self, input: tuple[str, list[InsertionRule]]) -> int:
        """ Returns the solution to part 2. """
        (polymer, rules) = input
        pair_freq_count = collections.Counter(a + b for (a, b) in sliding_window(polymer, 2))

        for step in range(0, 40):
            pair_freq_count = self.build_by_counts(pair_freq_count, rules)
            # print(f"After step {step+1}:")
            # print(pair_freq_count)

        freq_count = collections.defaultdict(int)
        for pair in pair_freq_count.keys():
            freq_count[pair[0]] += pair_freq_count[pair]
            freq_count[pair[1]] += pair_freq_count[pair]
        freq_count[polymer[0]] += 1
        freq_count[polymer[-1]] += 1
        for character in freq_count.keys():
            freq_count[character] //= 2

        max_count = max(freq_count.values())
        min_count = min(freq_count.values())

        # print(f"Final frequency count: {freq_count}")

        return max_count - min_count
