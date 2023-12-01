from ppsboot.utils.inputfile import InputFile
from ppsboot.utils.solution import Solution


class Day3(Solution):
    """ Day 3's solution. """

    def __init__(self):
        super().__init__(3, 'ppsboot/days/d03/input.txt')

    def load_input(self, filename: str) -> list[str]:
        """ Loads the input file. 
        
        Args:
            filename (str): The name of the input file.
        
        Returns:
            list: The input file as a list of strings.
        """
        return InputFile(filename).as_character_lists()

    def part1(self, input: list[str]) -> int:
        """ Solves part 1. 
        
        Transposing 2D lists: found 
        [here](https://stackoverflow.com/questions/6473679/transpose-list-of-lists)
        Mode of a list: found 
        [here](https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/)

        Args:
            input (list): The input file as a list of strings.
        
        Returns:
            int: The solution to part 1.
        """
        transposed_input = list(map(list, zip(*input)))
        most_common = list(map(lambda line : max(set(line), key=line.count), transposed_input))
        gamma = int(''.join(most_common), 2)

        least_common = list(map(lambda line : min(set(line), key=line.count), transposed_input))
        epsilon = int(''.join(least_common), 2)

        return gamma * epsilon