
from abc import abstractmethod
import time

from ppsboot.utils.exceptions import NotYetImplemented


class Solution:

    def __init__(self, day: int, filename: str) -> None:
        self._day = day
        self._filename = filename

    @abstractmethod
    def load_input(self, filename:str) -> list:
        """ Loads the input file. 
        
        Args:
            filename (str): The name of the input file.
        
        Returns:
            list: The input file as a list of strings.
        """
        with open(filename) as f:
            return f.readlines()

    @abstractmethod
    def part1(self, input: list) -> any:
        raise NotYetImplemented("Part 1 not yet implemented")

    @abstractmethod
    def part2(self, input: list) -> any:
        raise NotYetImplemented("Part 2 not yet implemented")

    @property
    def day(self) -> int:
        """ Returns the day. """
        return self._day

    @property
    def filename(self) -> str:
        """ Returns the filename. """
        return self._filename

    def _run_part(self, part: callable, number: int, input: list) -> None:
        """ Runs the part, times it, and prints output. """
        try:
            start = time.time()
            output = part(input)
            duration = time.time() - start
            print(f" Part {number}: {output} (run in {duration*1000:.2f} ms)")
        except NotYetImplemented as exc:
            output = str(exc)
            print(f" Part {number}: {output}")

    def run(self) -> None:
        """ Runs both parts of the solution. """
        input = self.load_input(self.filename)

        print(f"Day {self.day}:")
        self._run_part(self.part1, 1, input)
        self._run_part(self.part2, 2, input)
