#!/usr/bin/python3
""" The N queens puzzle is the challenge """
import sys


args = sys.argv
arg = ""
if len(args) == 2:
    arg = args[1]
else:
    print(Usage: nqueens N)
    exit(1)
try:
    arg = int(arg)
except ValueError:
    print("N must be a number")
    exit(1)
if (arg) < 4:
    print("N must be at least 4")
    exit(1)


