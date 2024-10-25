"""_summary_
reducer
"""

from __future__ import print_function
import sys


d1 = sys.stdin

r_id = None
k_counter = 0

for x in d1:
    x = x.replace("\n", "")
    if x != "":
        y = x.split("\t")
        if r_id != y[0]:
            if r_id:
                print(r_id + "\t" + str(k_counter))
            k_counter = 0
            r_id = y[0]
        k_counter += 1

if r_id:
    print(r_id + "\t" + str(k_counter))
