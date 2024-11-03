"""_summary_
mapper

0  | 1        | 2   | 3        | 4      | 5     | 6    | 7       | 8        | 9
id | uploader | age | category | length | views | rate | ratings | comments | related_ids

example_1:

for x in a1:
    x = x.replace("\n", "")
    if x != "":
        y = x.split("\t")
        for r in y[9:]:
            print(r, y[1])

"""

from __future__ import print_function
import sys
import os

if os.environ["mapred_task_is_map"] == "true":
    a1 = sys.stdin

    for x in a1:
        x = x.replace("\n", "")
        if x != "":
            y = x.split("\t")
            if len(y) > 9:
                print(str(y[3]) + "\t" + str(float(y[5]) * float(y[6])))
else:
    st = sys.stdin

    r_id = None
    r_counter = 0
    r_result = 0.0

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
