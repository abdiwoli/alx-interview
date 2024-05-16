#!/usr/bin/python3
""" Log Parsing Script """
import re
import sys


def parse_line(line):
    """ Parse a log line and extract relevant information """
    pattern = (
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
        r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
    )
    match = re.match(pattern, line)
    if match:
        return int(match.group(3)), int(match.group(4))
    else:
        return None, None


def print_statistics(total_size, status):
    """ Print statistics based on total size and status counts """
    print("Total file size:", sum(total_size))
    for code in sorted(status.keys()):
        if code in [200, 301, 400, 401, 403, 404, 405, 500]:
            print(f"{code}: {status[code]}")


if __name__ == "__main__":
    status = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    total_size = []
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            status_code, file_size = parse_line(line)
            if status_code is not None:
                status[status_code] = status.get(status_code, 0) + 1
                total_size.append(file_size)
                line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status)
                status = {200: 0, 301: 0, 400: 0, 401: 0,
                          403: 0, 404: 0, 405: 0, 500: 0}
                total_size = []
                line_count = 0

    except KeyboardInterrupt:
        print_statistics(total_size, status)
