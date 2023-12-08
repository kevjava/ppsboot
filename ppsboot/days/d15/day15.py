import math
from ppsboot.utils.solution import Solution


class Day15(Solution):

    def __init__(self) -> None:
        super().__init__(15, 'ppsboot/days/d15/input.txt')

    def load_input(self, filename: str) -> list[list[int]]:
        with open(filename, 'r') as f:
            grid = [[int(risk) for risk in line.strip()] for line in f.readlines()]
            return grid

    def print_grid(self, grid: list[list[int]]) -> None:
        for (i, row) in enumerate(grid):
            print(f"{i:3d} {''.join([str(i).ljust(4) for i in row])}")

    def score_grid(self, risks: list[list[int]]) -> int:
        distances = [[math.inf for _ in range(len(risks[0]))] for _ in range(len(risks))]
        start = (0, 0)
        end = (len(risks[0]) - 1, len(risks) - 1)

        distances[start[1]][start[0]] = 0
        queue = [start]

        while len(queue) > 0:
            (x, y) = queue.pop(0)
            current_distance = distances[y][x]

            if (x, y) == end:
                # self.print_grid(distances)
                return current_distance

            for (x2, y2) in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if x2 < 0 or x2 >= len(risks[0]) or y2 < 0 or y2 >= len(risks):
                    continue

                if current_distance + risks[y2][x2] < distances[y2][x2]:
                    distances[y2][x2] = current_distance + risks[y2][x2]
                    queue.append((x2, y2))

    def part1(self, grid: list[list[int]]) -> int:
        # print(grid)
        return self.score_grid(grid)

    def multiply_grid(self, grid: list[list[int]]) -> list[list[int]]:
        # print(grid)
        new_size = 5 * len(grid)
        new_grid = [[0 for _ in range(new_size)] for _ in range(new_size)]

        h = len(grid)
        for x in range(h):
            for y in range(h):
                for i in range(5):
                    for j in range(5):
                        new_grid[y + h * j][x + h * i] = grid[y][x] + i + j
                        if new_grid[y + h * j][x + h * i] > 9:
                            new_grid[y + h * j][x + h * i] -= 9
        return new_grid

    def part2(self, input: list[list[int]]) -> int:
        print("multiplying grid")
        grid = self.multiply_grid(input)
        # self.print_grid(grid)
        print("scoring")
        return self.score_grid(grid)
