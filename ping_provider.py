#!/usr/bin/python3

# reference : https://stackoverflow.com/questions/35750041/check-if-ping-was-successful-using-subprocess-in-python

import subprocess
import time

uptime = 0
downtime = 0

timestr = time.strftime("%Y%m%d-%H%M%S")

with open('ping_{}'.format(timestr), 'w') as f:
    while True:
        p = subprocess.Popen(['ping','8.8.8.8', '-c', '1'], stdout=subprocess.PIPE, universal_newlines = 1)

        for line in p.stdout:
            if "transmitted" in line or "unreachable" in line:
                f.write(line) 
                f.flush()

        time.sleep(5)
