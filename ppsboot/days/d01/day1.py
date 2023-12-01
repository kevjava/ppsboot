import collections
import itertools
from ppsboot.utils.inputfile import InputFile
from ppsboot.utils.solution import Solution

class Day1(Solution):

    def __init__(self) -> None:
        super().__init__(1, 'ppsboot/days/d01/input.txt')
    
    def load_input(self, filename:str) -> list:
        """ Loads the input file. 
        
        Args:
            filename (str): The name of the input file.
        
        Returns:
            list: The input file as a list of strings.
        """
        return InputFile(filename).as_single_ints()
        
    def part1(self, input: list) -> any:
        """ Solves part 1. 
        
        Args:
            input (list): The input file as a list of strings.
        
        Returns:
            any: The solution to part 1.
        """
        pairs = itertools.pairwise(input)
        increasing = list(filter(lambda pair: pair[1] > pair[0], pairs))
        return len(increasing)
    
    def sliding_window(self, iterable, n):
        """ Stolen mercilessly from 
        [here](https://docs.python.org/3/library/itertools.html#itertools-recipes) """
        # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
        it = iter(iterable)
        window = collections.deque(itertools.islice(it, n-1), maxlen=n)
        for x in it:
            window.append(x)
            yield tuple(window)

    def part2(self, input: list) -> any:
        """
        Args:
            input (list): The input file as a list of strings.
        
        Returns:
            any: The solution to part 2.
        """
        windows = self.sliding_window(input, 3)
        sums = map(sum, windows)
        pairs = itertools.pairwise(sums)
        increasing = list(filter(lambda pair: pair[1] > pair[0], pairs))
        return len(increasing)
