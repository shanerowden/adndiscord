from pathlib import Path
from adndiscord.utils import terminate, log
from random import randint

class AbilityScoreGen:
    """
    Generates six unallocated ability scores using variety of
    techniques common to the d20 RPG system. The default behaviour 
    rolls 3d6 six times.
    """
    DEFAULT_DQ = 3
    DEFAULT_DS = 6
    DEFAULT_DT = 6

    DEFAULT_MIN = 3
    DEFAULT_MAX = 18

    def __repr__(self):
        return f"AbilityScoreGen(rolls={self.final})"


    def __init__(
        self, d_quan: int = DEFAULT_DQ,
              d_times: int = DEFAULT_DT):
        """
        :d_quan: for each increment over default, 
                    subtracts one die with lowest value
        :d_times: for each increment over default, 
                    rolls total another time and removes lowest value from all rolls
        :return: a tuple containing six integers between DEFAULT_MIN and DEFAULT_MAX
        """
        self.all_rolls = []
        self.d_quan = d_quan
        self.d_times = d_times

        # Difference from Total Die Per Roll to Dropped Die Count
        self.quan_difference = self.get_difference(d_quan, AbilityScoreGen.DEFAULT_DQ)
        self.times_difference = self.get_difference(d_times, AbilityScoreGen.DEFAULT_DT)

        self.roll_all(d_quan, d_times)
        
        self.final = self.all_rolls

    @staticmethod
    def get_difference(value: int, default: int) -> int:
        if value == default:
            return 0
        elif value > default:
            return value - default
        elif value < default:
            log(f"This might shouldn't be less than {default}", "info")
            return default - value
        else:
            terminate("Check 'get_difference Call'")

    @staticmethod
    def roll_one(modifier: int = 0) -> tuple:
        result = randint(1, AbilityScoreGen.DEFAULT_DS)
        return result, result + modifier

    def roll_set(self, times: int) -> int:
        rolled_set = []
        for i in range(times):
            roll, modified_roll = self.roll_one()
            print(f"Rolled set: {roll}; +MODIFIER: {modified_roll}")
            rolled_set.append(modified_roll)
        for i in range(self.quan_difference):
            lowest = min(rolled_set)
            print(f"Removing {lowest}")
            rolled_set.remove(lowest)
        for roll in rolled_set:
            print(roll, end=" ")
        return sum(rolled_set)

    def roll_all(self, dice_per_set: int, total_rolls: int):
        for i in range(total_rolls):
            rolled = self.roll_set(dice_per_set)
            print(f"Rolled: {rolled}")
            self.all_rolls.append(rolled)
        for i in range(self.times_difference):
            lowest = min(self.all_rolls)
            print(f"Removing {lowest}")
            self.all_rolls.remove(lowest)


