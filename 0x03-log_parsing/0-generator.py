#!/usr/bin/python3
import sys
from time import sleep

# Predefined log entries
log_entries = [
    "166.152.170.40 - [2017-02-05 23:28:50.535640] \"GET /projects/260 HTTP/1.1\" 405 977\n",
    "58.70.209.187 - [2017-02-05 23:28:50.564010] \"GET /projects/260 HTTP/1.1\" 401 708\n",
    "125.218.201.102 - [2017-02-05 23:28:51.484960] \"GET /projects/260 HTTP/1.1\" 500 684\n",
    "93.202.122.198 - [2017-02-05 23:28:52.060026] \"GET /projects/260 HTTP/1.1\" 500 1002\n",
    "83.93.222.77 - [2017-02-05 23:28:52.920758] \"GET /projects/260 HTTP/1.1\" 200 551\n",
    "186.161.131.204 - [2017-02-05 23:28:53.006680] \"GET /projects/260 HTTP/1.1\" 500 665\n",
    "61.146.36.164 - [2017-02-05 23:28:53.792909] \"GET /projects/260 HTTP/1.1\" 401 299\n",
    "70.139.77.18 - [2017-02-05 23:28:54.747004] \"GET /projects/260 HTTP/1.1\" 403 543\n",
    "241.71.80.100 - [2017-02-05 23:28:55.573972] \"GET /projects/260 HTTP/1.1\" 500 222\n",
    "219.109.138.129 - [2017-02-05 23:28:55.755290] \"GET /projects/260 HTTP/1.1\" 200 186\n",
    "118.99.189.189 - [2017-02-05 23:28:56.091266] \"GET /projects/260 HTTP/1.1\" 403 278\n"
]

# Loop through each log entry
for entry in log_entries:
    sys.stdout.write(entry)
    sys.stdout.flush()
    # Introduce a slight delay between log entries
    sleep(0.1)
