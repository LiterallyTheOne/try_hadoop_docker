"""reducer"""

from __future__ import print_function
import sys


def main():
    """main function"""

    r1 = None
    r2 = None
    r_counter = 0

    for x in sys.stdin:
        x = x.replace("\n", "")

        if x == "":
            continue

        y = x.split("\t")

        if r1 != y[0] or r2 != y[1]:
            if r1 and r2:
                print(r1 + " " + r2 + "\t" + str(r_counter))

            r1 = y[0]
            r2 = y[1]
            r_counter = 0

        r_counter += 1

    if r1 and r2:
        print(r1 + " " + r2 + "\t" + str(r_counter))


if __name__ == "__main__":
    main()
