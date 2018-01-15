# This module describe monitoring for Different Pools
import config
import os
import re

def grepmonitor():
    list1 = []
    output = ""

    a = str(os.popen("crontab -l | grep nicehash").readlines())
    if re.match(r'^\[\'\#', a):
        a = "Nicehash Monitor - DISABLED"
        list1.append(a)
    else:
        a = "Nicehash Monitor - ENABLED"
        list1.append(a)

    b = str(os.popen("crontab -l | grep zecnanomonitor").readlines())
    if re.match(r'^\[\'\#', b):
        b = "ZEC Nano Monitor - DISABLED"
        list1.append(b)
    else:
        b = "ZEC Nano Monitor - ENABLED"
        list1.append(b)

    c = str(os.popen("crontab -l | grep xfxnanomonitor").readlines())
    if re.match(r'^\[\'\#', c):
        c = "XFX Nano Monitor - DISABLED"
        list1.append(c)
    else:
        c = "XFX Nano Monitor - ENABLED"
        list1.append(c)

    d = str(os.popen("crontab -l | grep saphirenanomon").readlines())
    if re.match(r'^\[\'\#', d):
        d = "SAPH Nano Monitor - DISABLED"
        list1.append(d)
    else:
        d = "SAPH Nano Monitor - ENABLED"
        list1.append(d)

    print list1

    for i in list1:
        output = output + str(i) + "\n"
    return output

