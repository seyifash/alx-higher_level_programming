#!/usr/bin/python3
for char_code in range(ord('Z'), ord('A') - 1, -1):
    print(chr(char_code + 32 if char_code % 2 == 0 else char_code), end='')
