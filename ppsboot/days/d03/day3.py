from ppsboot.utils.solution import Solution


class Day3(Solution):
    """ Day 3's solution. """

    def __init__(self):
        super().__init__(3, 'ppsboot/days/d03/input.txt')

    def load_input(self, filename: str) -> list[str]:
        with open(self._filename) as f:
            return [list(line.strip()) for line in f.readlines()]

    def find_most_common(self, line: list[str]) -> str:
        """
        Converts the line to a set of characters, then finds the one with the highest count,
        using `max`. Inspired by code found
        [here](https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/)
        The reverse sort makes sure the ones break the tie (in the case of a tie, max returns
        the first one).
        """
        return max(sorted(list(set(line)), reverse=True), key=line.count)

    def find_least_common(self, line: list[str]) -> str:
        """
        Converts the line to a set of characters, then finds the one with the lowest count,
        using `min`.  The sort order makes sure zeros break the tie.
         """
        return min(sorted(list(set(line))), key=line.count)

    def part1(self, input: list[str]) -> int:
        """
        Transposing 2D lists: found
        [here](https://stackoverflow.com/questions/6473679/transpose-list-of-lists)
        Mode of a list: found
        """
        # transposed_input = list(map(list, zip(*input)))
        transposed_input = [list(x) for x in zip(*input)]
        most_common_chars = [self.find_most_common(x) for x in transposed_input]
        gamma = int(''.join(most_common_chars), 2)

        # least_common_chars = list(map(self.find_least_common, transposed_input))
        least_common_chars = [self.find_least_common(x) for x in transposed_input]
        epsilon = int(''.join(least_common_chars), 2)

        return gamma * epsilon

    def part2(self, input: list[str]) -> int:
        """

        """
        matching_values = [''.join(x) for x in input]
        prefix, digit = '', 0
        while len(matching_values) > 1:
            digits_to_compare = [x[digit] for x in matching_values]
            prefix += self.find_most_common(digits_to_compare)
            digit += 1
            matching_values = [x for x in matching_values if x.startswith(prefix)]
        oxygen_generator_rating = int(''.join(matching_values[0]), 2)

        matching_values = [''.join(x) for x in input]
        prefix, digit = '', 0
        while len(matching_values) > 1:
            digits_to_compare = [x[digit] for x in matching_values]
            prefix += self.find_least_common(digits_to_compare)
            digit += 1
            matching_values = [x for x in matching_values if x.startswith(prefix)]
        co2_scrubber_rating = int(''.join(matching_values[0]), 2)

        return oxygen_generator_rating * co2_scrubber_rating
