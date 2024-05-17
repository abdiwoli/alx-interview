#!/usr/bin/python3
""" import module """
import sys
import re
from collections import defaultdict


def is_valid_input(input_string):
    """Checks if a line matches the expected access log format a.
    """
    pattern = r"^(\S+) - \[.*?\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$"
    match = re.match(pattern, input_string.strip())
    if match:
        try:
            status_code = int(match.group(2))
            file_size = int(match.group(3))
            return True, status_code, file_size
        except ValueError:
            pass
    return False, None, None


def print_out(total_size, status):
    """Prints the calculated statistics"""
    print(f"File size: {sum(total_size)}")
    for code, count in sorted(status.items()):
        print(f"{code}: {count}")


if __name__ == "__main__":
    status = dict()
    total_size = []
    line_count = 0
    remain = False
    try:
        for line in sys.stdin:
            line_count += 1
            is_valid, status_code, file_size = is_valid_input(line)
            ramain = True
            if is_valid:
                total_size.append(file_size)
                status[status_code] = status.get(status_code, 0) + 1
            if line_count % 10 == 0:
                print_out(total_size, status)
                remain = False
    except KeyboardInterrupt:
        print_out(total_size, status)
        raise
    if remain:
        print_out(total_size, status)
        
