#!/usr/bin/python3
""" interview """


def minOperations(n):
    """ min operations"""
    text = "H"
    op = ["copy", "paste"]
    count = 0
    for i, o in enumerate(op):
        if o == "paste":
            text += text
        if len(text) == n:
            return i
