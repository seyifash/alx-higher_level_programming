#!/usr/bim/python3
def complex_delete(a_dictionary, value):
    listofkeys = list(a_dictionary.keys())

    for values in listofkeys:
        if value == a_dictionary.get(values):
            del a_dictionary(values)
        return a_dictionary
