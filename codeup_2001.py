# Codeup_그리디_2001: 최소 대금

import sys
pasta = 2001
juice = 2001
for i in range(3):
    pasta = min(pasta, int(sys.stdin.readline()))
for i in range(2):
    juice = min(juice, int(sys.stdin.readline()))
hap = pasta + juice
hap += hap*0.1
print(round(hap, 1))