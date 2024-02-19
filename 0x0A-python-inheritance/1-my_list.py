#!/usr/bin/python3
"""
    Definition of the file module for 1-my_list
"""


class MyList(list):
    """MyList class entity definition"""

    def print_sorted(self):
        """Print sprted list without changing original"""
        copy = self.copy()
        copy.sort()
        print(copy)
