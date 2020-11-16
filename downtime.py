import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
args = parser.parse_args()

uptime = 0
downtime = 0

for f in args.file:
    for line in f:
        if "1 packets received" in line:
            uptime = uptime + 5
        else:
            downtime = downtime + 5

percent_down = downtime/uptime * 100

print("total uptime is {} seconds".format(uptime))
print("total downtime is {} seconds".format(downtime))
print("downtime % = {:.2f}".format(percent_down))

