__author__ = 'carl.alexandersson'

import sys
from time import sleep
from datetime import datetime

time = datetime.now()
s = time.second
m = time.minute
h = time.hour

for x in xrange(sys.maxint):
    s += 1
    if s == 60:
        s -= 60
        m += 1
    if m == 60:
        m -= 60
        h += 1
    if h < 10 and m < 10 and s < 10:
        print "0%d:0%d:0%d" % (h, m, s)
    elif h < 10 and m < 10 <= s:
        print "0%d:0%d:%d" % (h, m, s)
    elif h < 10 and m >= 10 <= s:
        print "0%d:%d:%d" % (h, m, s)
    elif h < 10 and m >= 10 > s:
        print "0%d:%d:0%d" % (h, m, s)
    elif h >= 10 and m < 10 > s:
        print "%d:0%d:0%d" % (h, m, s)
    elif h >= 10 and m < 10 <= s:
        print "%d:0%d:%d" % (h, m, s)
    elif h >= 10 and m >= 10 > s:
        print "%d:%d:0%d" % (h, m, s)
    else:
        print "%d:%d:%d" % (h, m, s)
    sleep(1)
