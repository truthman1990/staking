import argparse
import re
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
args = parser.parse_args()

uptime = 0
downtime = 0

for f in args.file:
    for line in f:
        sentence = bool(re.search(', 1 ?\S* received', line))

        if sentence:
            uptime = uptime + 5
        else:
            downtime = downtime + 5

percent_down = downtime/uptime * 100

#uptime_minutes = str(datetime.timedelta(seconds=uptime))

print("total uptime is {}".format(str(datetime.timedelta(seconds=uptime))))
print("total downtime is {}".format(str(datetime.timedelta(seconds=downtime))))
print("downtime % = {:.2f}".format(percent_down))

