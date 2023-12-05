from collections import Counter, defaultdict
import re
from ppsboot.utils.solution import Solution


class Day12(Solution):
    def __init__(self):
        super().__init__(12, 'ppsboot/days/d12/input.txt')

    big_caves = re.compile('[A-Z]')
    small_caves = re.compile('[a-z]')

    def load_input(self, filename: str) -> list[tuple[str, str]]:
        with open(filename) as f:
            return [line.strip().split('-') for line in f.readlines()]

    def traverse_paths(self, paths: dict[str, str], current_path: list[str]) -> list[list[str]]:
        """
        Returns all possible paths through the cave. Big caves can be visited infinitely,
        but small caves can only be visited once.
        """
        current_node = current_path[-1]
        if current_node == 'end':
            yield current_path
            return

        for next_node in paths[current_node]:
            if next_node not in current_path or self.big_caves.match(next_node):
                yield from self.traverse_paths(paths, current_path + [next_node])

    def part1(self, input: list[tuple[str, str]]) -> int:
        """ Returns the solution to part 1. """
        paths: dict[str, str] = defaultdict(list[str])

        for (start, end) in input:
            paths[start].append(end)
            paths[end].append(start)

        possible_paths = list(self.traverse_paths(paths, ['start']))
        # [print(",".join(path)) for path in possible_paths]
        return len(possible_paths)

    def traverse_more_paths(self,
                            paths: dict[str, str],
                            current_path: list[str]) -> list[list[str]]:
        """ Returns all possible paths through the cave, but we can visit small caves twice now. """
        current_node = current_path[-1]
        if current_node == 'end':
            yield current_path
            return

        # Filter our path for small caves, and count how many times we've visited the most common.
        small_caves = list(filter(lambda cave: self.small_caves.match(cave), current_path))
        visit_count = Counter(small_caves).most_common()[0][1]

        for next_node in paths[current_node]:
            if 'start' == next_node:
                continue

            if next_node not in current_path or \
                    (visit_count < 2 and next_node in current_path) or \
                    (visit_count == 2 and next_node not in current_path) or \
                    self.big_caves.match(next_node):
                yield from self.traverse_more_paths(paths, current_path + [next_node])

    def part2(self, input: list[tuple[str, str]]) -> int:
        """ Returns the solution to part 2. """
        paths: dict[str, str] = defaultdict(list[str])

        for (start, end) in input:
            paths[start].append(end)
            paths[end].append(start)

        possible_paths = list(self.traverse_more_paths(paths, ['start']))
        # [print(",".join(path)) for path in possible_paths]
        return len(possible_paths)
