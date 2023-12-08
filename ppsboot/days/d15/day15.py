from dataclasses import dataclass
import sys
from ppsboot.utils.solution import Solution


@dataclass
class Node:
    x: int
    y: int
    risk: int
    distance: int = sys.maxsize
    visited: bool = False

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Grid:

    __nodes: list[list[Node]]
    __queue: list[Node]

    def __init__(self, grid: list[list[int]]) -> None:
        self.__nodes = [[Node(x, y, grid[y][x])
                         for x in range(len(grid[y]))]
                        for y in range(len(grid))]

    def __str__(self) -> str:
        return '\n'.join([''.join([str(node.risk) for node in row]) for row in self.__nodes])

    def __get_adjacent_nodes(self, node: Node) -> list[Node]:
        adjacent_nodes = []
        for x, y in [(node.x - 1, node.y), (node.x, node.y - 1),
                     (node.x + 1, node.y), (node.x, node.y + 1)]:
            if 0 <= x < len(self.__nodes[0]) and 0 <= y < len(self.__nodes):
                if not self.__nodes[y][x].visited:
                    adjacent_nodes.append(self.__nodes[y][x])
        # print("Adjacent nodes: ", adjacent_nodes)
        return adjacent_nodes

    def get_end_distance(self) -> int:
        return self.__nodes[-1][-1].distance

    def height(self) -> int:
        return len(self.__nodes)

    def value_at(self, x: int, y: int) -> int:
        return self.__nodes[y][x].risk

    def score(self) -> None:
        self.__nodes[0][0].risk = 0  # First one has no risk
        self.__nodes[0][0].distance = 0  # First one has no distance
        self.__queue: list[Node] = [self.__nodes[0][0]]
        while len(self.__queue) > 0:
            this_node = self.__queue.pop(0)
            # print(f"Visiting {this_node.x}, {this_node.y} with risk {this_node.risk} and "
            #       f"distance {this_node.distance}")
            for next_node in self.__get_adjacent_nodes(this_node):
                next_node.distance = min([next_node.distance, next_node.risk + this_node.distance])
                if (next_node not in self.__queue) and (not next_node.visited):
                    # print(f"Queuing node {next_node.x}, {next_node.y} with distance "
                    #       f"{next_node.distance}")
                    self.__queue.append(next_node)
            this_node.visited = True


class Day15(Solution):

    def __init__(self) -> None:
        super().__init__(15, 'ppsboot/days/d15/input_test.txt')

    def load_input(self, filename: str) -> Grid:
        with open(filename, 'r') as f:
            grid = Grid([[int(c) for c in line.strip()] for line in f.readlines()])
            return grid

    def part1(self, grid: Grid) -> int:
        # print(grid)
        grid.score()
        return grid.get_end_distance()

    def multiply_grid(self, grid: Grid) -> Grid:
        # print(grid)
        new_size = 5 * grid.height()
        new_grid = [[0 for _ in range(new_size)] for _ in range(new_size)]
        for x in range(grid.height()):
            for y in range(grid.height()):
                new_grid[y][x] = grid.value_at(x, y)

        h = grid.height()
        for x in range(h):
            for y in range(h):
                for i in range(5):
                    for j in range(5):
                        new_grid[y + h * j][x + h * i] = grid.value_at(x, y) + i + j
                        if new_grid[y + h * j][x + h * i] > 9:
                            new_grid[y + h * j][x + h * i] -= 9

        return Grid(new_grid)

    def part2(self, input: Grid) -> int:
        grid = self.multiply_grid(input)
        print(grid)
        grid.score()
        return grid.get_end_distance()
