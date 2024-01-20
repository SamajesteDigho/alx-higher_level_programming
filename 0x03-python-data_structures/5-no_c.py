#!/usr/bin/python3
def no_c(my_string):
    str = "".join(x for x in my_string if x not in 'cC')
    return str
