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


a1 = sys.stdin


r_id = None
k_counter = 0

sum_k = 0

for x in a1:
    x = x.replace("\n", "")
    if x != "":
        y = x.split("\t")
        if r_id != y[0]:
            if r_id:
                print(r_id + "\t" + str(sum_k) + "\t" + str(k_counter))

            r_id = y[0]
            k_counter = 0
            sum_k = 0
        k_counter += 1
        sum_k += float(y[1])


if r_id:
    print(r_id + "\t" + str(sum_k) + "\t" + str(k_counter))

# for x, y in d1.items():
#     sum_1 = 0
#     for z in y:
#         sum_1 += float(z)

#     print(x, sum_1, len(y), sep="\t")
