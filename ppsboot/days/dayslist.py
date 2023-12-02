from ppsboot.days.d01.day1 import Day1
from ppsboot.days.d02.day2 import Day2
from ppsboot.days.d03.day3 import Day3
from ppsboot.days.d04.day4 import Day4
from ppsboot.days.d05.day5 import Day5
from ppsboot.utils.solution import Solution


class Days:

    _days: list[Solution]
    _daysByDay: dict[int, Solution]

    def __init__(self):
        self._days = []
        self._daysByDay = {}
        self.add(Day1())
        self.add(Day2())
        self.add(Day3())
        self.add(Day4())
        self.add(Day5())

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
