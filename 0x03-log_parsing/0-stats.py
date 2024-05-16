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


def print_out(total_size, status):
    """ print the output """
    print("File size: {:d}".format(sum(total_size)))
    for k, v in sorted(status.items()):
        print(f"{k}: {v}")


if __name__ == "__main__":
    status = dict()
    total_size = []
    line_count = 0
    try:
        for line in sys.stdin:
            key, size = is_valid(line.strip())
            if key and size:
                val = status.get(key, 0)
                status[key] = val + 1
                total_size.append(size)
                line_count += 1
            if line_count % 10 == 0:
                print_out(total_size, status)
                status.clear()
                total_size.clear()
                line_count = 0

    # Check if there are any remaining lines to process
            if line_count > 0:
                print_out(total_size, status)
    except KeyboardInterrupt:
        print_out(total_size, status)
        raise
