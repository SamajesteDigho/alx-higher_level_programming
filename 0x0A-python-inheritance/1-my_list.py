#!/usr/bin/python3
"""
    Definition of the file module for 1-my_list
"""


class MyList(list):
    """MyList class entity definition"""

    def __init__(self):
        """Initialization of the function"""
        super().__init__()

    def print_sorted(self):
        """Print sprted list without changing original"""
        copy = self.copy()
        copy.sort()
        print("{}".format(copy))
