#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delkeys = [keys for keys, val in a_dictionary.items() if value == val]
    for keys in delkeys:
        del a_dictionary[keys]
    return a_dictionary
