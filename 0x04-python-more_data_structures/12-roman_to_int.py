#!/usr/bin/python3
def roman_to_int(roman_string):
    rval = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    N = len(roman_string)
    i = N - 1
    output = 0
    while i >= 0:
        if i < N - 1 and rval[roman_string[i]] < rval[roman_string[i + 1]]:
            output -= rval[roman_string[i]]
        else:
            output += rval[roman_string[i]]
        i -= 1
    return output
