#!/usr/bin/python3
"""
    Module for the MyInt class
"""


class MyInt(int):
    """Definition for the MyInt class"""

    def __eq__(self, __value: object) -> bool:
        """Rebellion of equal to"""
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        """Rebellion of not equal to"""
        return super().__eq__(__value)
