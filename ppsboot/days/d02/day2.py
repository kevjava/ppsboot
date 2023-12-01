
from functools import reduce
from ppsboot.utils.inputfile import InputFile
from ppsboot.utils.solution import Solution

class Day2(Solution):
    """ Day 2's solution. 
    
    Problem statement is [here](https://adventofcode.com/2021/day/2).
    """

    def __init__(self):
        super().__init__(2, 'ppsboot/days/d02/input.txt')

    def load_input(self, filename:str) -> tuple[str, int]:
        """ Loads the input file. 
        
        Args:
            filename (str): The name of the input file.
        
        Returns:
            list: The input file as a list of strings.
        """
        tuples = InputFile(filename).as_tuples()
        return map(lambda t: (t[0], int(t[1])), tuples)

    def calculate_position(self, position: tuple[int, int], 
                           instruction: tuple[str, int]) -> tuple[int, int]:
        """ Calculates and returns the new position given the current position and an 
        instruction.
        
        Args:
            position (tuple[int, int]): The current position (x,y).
            instruction (tuple[str, int]): The instruction (either forward, down, or up).
        
        Returns:
            tuple[int, int]: The new position.
        """
        (x, y) = position
        (direction, distance) = instruction
        if direction == 'forward':
            return (x + distance, y)
        elif direction == 'down':
            return (x, y + distance) # Down increases your depth.
        elif direction == 'up':
            return (x, y - distance)
        else:
            return position 

    def part1(self, input: tuple[str, int]) -> int:
        """ Solves part 1. 
        
        Args:
            input (tuple[str, int]): The input file as a list of strings.
        
        Returns:
            int: The solution to part 1 - the final coordinate's x times y.
        """
        (new_x, new_y) = reduce(self.calculate_position, input, (0,0) )
        return new_x * new_y
