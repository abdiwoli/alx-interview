#!/usr/bin/python3
import sys
from time import sleep

# Predefined log entries
log_entries = []

with open("logfile.txt", "r") as file:
    for line in file:
        log_entries.append(line.strip())


# Loop through each log entry
for entry in log_entries:
    sys.stdout.write(entry)
    sys.stdout.flush()
    # Introduce a slight delay between log entries
    sleep(0.1)
