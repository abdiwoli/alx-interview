#!/usr/bin/python3
""" std parsing """
import re
import sys


def is_valid(input_string):
    """ is valid input """
    pattern = (
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
        r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')
    regex = re.compile(pattern)
    match = regex.match(input_string)
    if match:
        try:
            status_code = int(match.group(3))
            file_size = int(match.group(4))
        except TypeError as e:
            return None, None
        return status_code, file_size
    else:
        return None, None


status = dict()
total_size = []
for line in sys.stdin:
    key, size = is_valid(line)
    if key and size:
        val = status.get(key, 0)
        status[key] = val + 1
        total_size.append(size)
    if len(total_size) == 10:
        print(f"File size: {sum(total_size)}")
        for i in status.keys():
            print(f"{i}: {status[i]}")
        status.clear()
        total_size.clear()
