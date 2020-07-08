import logging
from pathlib import Path
from adndiscord.utils import terminate


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
    
    def __init__(
        self, d_quan: int = DEFAULT_DQ,
              d_times: int = DEFAULT_DT) -> tuple:
        """
        :d_quan: for each increment over default, 
                    subtracts one die with lowest value
        :d_times: for each increment over default, 
                    rolls total another time and removes lowest value from all rolls
        :return: a tuple containing six integers between DEFAULT_MIN and DEFAULT_MAX
        """

        # Difference from Total Die Per Roll to Dropped Die Count
        if d_quan == AbilityScoreGen.DEFAULT_DQ:
            difference = 0
        elif d_quan > AbilityScoreGen.DEFAULT_DQ:
            difference = d_quan - AbilityScoreGen.DEFAULT_DQ
        elif d_quan < AbilityScoreGen.DEFAULT_DQ:
            difference = AbilityScoreGen.DEFAULT_DQ - d_quan
        else:
            terminate("Check \n\t 'Difference from Total Die Per Roll to Dropped Die Count'")
            
            
        
    def roll_set(self, roll_count: int, pop_lowest_count: int, modifier: int) -> int:
        pass
        
        
