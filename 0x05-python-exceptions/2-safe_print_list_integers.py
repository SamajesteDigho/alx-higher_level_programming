#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for elt in my_list[:x]:
        try:
            print("{:d}".format(elt), end='')
            count += 1
            if count > x:
                raise IndexError
        except IndexError as e:
            print("{}".format(e), end='')
        except Exception:
            print('', end='')
    print("")
    return count
