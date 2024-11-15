"""
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


def main():
    """main function"""
    a1 = sys.stdin

    for x in a1:
        x = x.replace("\n", "")
        if x != "":
            y = x.split("\t")
            if len(y) > 9:
                print(str(y[3]) + "\t" + str(float(y[5]) * float(y[6])))


if __name__ == "__main__":
    main()
