#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for elt in my_list[:x]:
            print("{}".format(elt), end='')
            count += 1
    except Exception:
        pass
    finally:
        print("")
        return count
