
import sys
from ppsboot.days.dayslist import Days
from ppsboot.main import PPSBootCamp


if __name__ == "__main__":

    if (len(sys.argv)) > 1:
        if (sys.argv[1].isnumeric()):
            day_number = int(sys.argv[1])
        else:
            print(f"Invalid day number: {sys.argv[1]}")
            sys.exit(1)

        solution = Days().getByDay(day_number)
        if solution:
            solution.run()
        else:
            print(f"Day {day_number} not found")
    else:
        PPSBootCamp().run()
