#!/usr/bin/python3
""" import module """
import sys
import re
from collections import defaultdict


def is_valid_input(input_string):
    """Checks if a line matches the expected access log format."""
    pat = r"^(\S+)\s*-\s*\[.*?\] \"GET /projects/260 HTTP/1.1\" (\S+) (\d+)$"
    match = re.match(pat, input_string.strip())
    status_code = None
    file_size = None
    if match:
        try:
            status_code = int(match.group(2))
        except ValueError:
            status_code = None
        try:
            file_size = int(match.group(3))
        except ValueError:
            file_size = None
    return status_code, file_size


def print_out(total_size, status):
    """Prints the calculated statistics."""
    if not total_size and not status:
        return
    print(f"File size: {sum(total_size)}")
    for code, count in sorted(status.items()):
        print(f"{code}: {count}")


if __name__ == "__main__":
    status = defaultdict(int)
    total_size = []
    line_count = 0
    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = is_valid_input(line)
            if status_code and file_size:
                total_size.append(file_size)
                status[status_code] += 1
            elif file_size:
                total_size.append(file_size)
            if line_count % 10 == 0:
                print_out(total_size, status)
        # Print remaining output if file is not empty
        if line_count % 10 != 0:
            print_out(total_size, status)
    except KeyboardInterrupt:
        print_out(total_size, status)
        raise
