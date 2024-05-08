#!/usr/bin/python3
""" interview """


def minOperations(n):
    """ min operations"""
    text = "H" * n
    count = 0
    flag = 0
    while(len(text) > 1):
        ln = len(text)
        if ln % 2 == 1:
            flag = 1
        text = text[:ln // 2]
        count += 2
    return count + flag
