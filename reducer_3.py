"""_summary_
reducer
"""

from __future__ import print_function
import sys


st = sys.stdin


r_id = None
r_counter = 0
r_result = 0


for x in st:
    x = x.replace("\n", "")
    if x != "":
        y = x.split("\t")

        if r_id != y[0]:
            if r_id:
                r_result /= r_counter
                print(r_id + "\t" + str(r_result))

            r_id = y[0]
            r_counter = 0
            r_result = 0

        r_counter += int(y[2])
        r_result += float(y[1])


if r_id:
    r_result /= r_counter
    print(r_id + "\t" + str(r_result))
