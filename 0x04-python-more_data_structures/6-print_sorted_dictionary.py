#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_items = sorted(a_dictionary)
    for key in sorted_items:
        print("{}: {}".format(key, a_dictionary[key]))
