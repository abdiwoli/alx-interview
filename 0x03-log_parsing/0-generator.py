#!/usr/bin/python3
import sys
from time import sleep

# Predefined log entries
log_entries = [

]

# Loop through each log entry
for entry in log_entries:
    sys.stdout.write(entry)
    sys.stdout.flush()
    # Introduce a slight delay between log entries
    sleep(0.1)
