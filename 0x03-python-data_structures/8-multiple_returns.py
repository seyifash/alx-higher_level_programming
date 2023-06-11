#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        length = len(sentence)
        firstchar = sentence[0]
        tups = length, firstchar
        return (tups)
    else:
        return (0, None)
