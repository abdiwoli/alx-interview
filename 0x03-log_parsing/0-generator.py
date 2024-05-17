#!/usr/bin/python3
import sys
from time import sleep

# Predefined log entries
log_entries = [
    "68.249.9.20 - [2017-02-05 23:31:22.452556] \"GET /projects/260 HTTP/1.1\" 200 711\n",
    "Hello\n",
    "99.196.100.39 - [2017-02-05 23:31:22.954433] \"GET /projects/260 HTTP/1.1\" 401 658\n",
    "128.230.61.246 - [2017-02-05 23:31:23.258076] \"GET /projects/260 HTTP/1.1\" Hello 292\n",
    "116.82.223.35 - [2017-02-05 23:31:24.112360] \"GET /projects/260 HTTP/1.1\" 301 842\n",
    "Holberton - [2017-02-05 23:31:25.003550] \"GET /projects/260 HTTP/1.1\" 400 12\n",
    "7.179.133.121 - [2017-02-05 23:31:25.003550] \"GET /projects/260 HTTP/1.1\" 400 12\n",
    "188.213.11.218-[2017-02-05 23:31:21.690755] \"GET /projects/260 HTTP/1.1\" 401 1000\n",
    "128.230.61.246 - [2017-02-05 23:31:23.258076] \"GET /projects/260 HTTP/1.1\" 301 292\n"
]

# Loop through each log entry
for entry in log_entries:
    sys.stdout.write(entry)
    sys.stdout.flush()
    # Introduce a slight delay between log entries
    sleep(0.1)
