#!/usr/bin/python3
"""
    Here is the module for the exercise 5-text_indentation
    functions:
        text_indentation(text):
"""


def text_indentation(text):
    """
        This function printing with indentation
    """
    broken = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for car in text:
        if car in ['.', '?', ':']:
            print('{}\n\n'.format(car), end='')
            broken = True
        elif broken and car == ' ':
            pass
        else:
            broken = False
            print('{}'.format(car), end='')
    print("")
