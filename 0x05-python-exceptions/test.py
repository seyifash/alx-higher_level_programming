#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    listcount = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                listcount += 1
            except ValueError:
                continue
    except TypeError:
        pass
    finally:
        print()
    return listcount
