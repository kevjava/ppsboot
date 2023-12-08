from ppsboot.days.d01.day1 import Day1
from ppsboot.days.d02.day2 import Day2
from ppsboot.days.d03.day3 import Day3
from ppsboot.days.d04.day4 import Day4
from ppsboot.days.d05.day5 import Day5
from ppsboot.days.d06.day6 import Day6
from ppsboot.days.d07.day7 import Day7
from ppsboot.days.d08.day8 import Day8
from ppsboot.days.d09.day9 import Day9
from ppsboot.days.d10.day10 import Day10
from ppsboot.days.d11.day11 import Day11
from ppsboot.days.d12.day12 import Day12
from ppsboot.days.d13.day13 import Day13
from ppsboot.days.d14.day14 import Day14
from ppsboot.utils.solution import Solution


class Days:

    _days: list[Solution]
    _daysByDay: dict[int, Solution]

    def __init__(self):
        self._days = []
        self._daysByDay = {}
        # TODO: Add a crawler that discovers these.
        self.add(Day1())
        self.add(Day2())
        self.add(Day3())
        self.add(Day4())
        self.add(Day5())
        self.add(Day6())
        self.add(Day7())
        self.add(Day8())
        self.add(Day9())
        self.add(Day10())
        self.add(Day11())
        self.add(Day12())
        self.add(Day13())
        self.add(Day14())

    def add(self, day: Solution) -> None:
        """ Adds a day.

        Args:
            day (Solution): The day's solution to add.
        """
        self._days.append(day)
        self._daysByDay[day.day] = day

    def getByDay(self, day: int) -> Solution | None:
        """ Returns the day with the given number.

        Args:
            day (int): The day number.

        Returns:
            Solution: The day's solution.
        """
        if day not in self._daysByDay:
            return None
        return self._daysByDay[day]
