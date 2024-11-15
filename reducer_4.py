"""reducer"""

from __future__ import print_function
import sys


def main():
    """main function"""
    st = sys.stdin

    r_id = None
    r_result = 0

    for x in st:
        x = x.replace("\n", "")

        if x == "":
            continue

        y = x.split("\t")

        if r_id != y[0]:
            if r_id:
                print(r_id + "\t" + str(r_result))

            r_id = y[0]
            r_result = 0

        r_result += int(y[1])

    if r_id:
        print(r_id + "\t" + str(r_result))


if __name__ == "__main__":
    main()
