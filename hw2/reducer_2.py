"""reducer"""

from __future__ import print_function
import sys


def main():
    """main function"""
    d1 = sys.stdin

    r_id = None
    k_counter = 0

    p = None
    p_counter = 0

    for x in d1:
        x = x.replace("\n", "")
        if x != "":
            y = x.split("\t")
            if r_id != y[0]:
                if p != y[1]:
                    p = y[1]
                    p_counter = 0

                if r_id:
                    print(r_id + "\t" + str(k_counter))
                k_counter = 0
                r_id = y[0]
            p_counter += 1
            if p_counter > 1:
                k_counter += 1

    if r_id:
        print(r_id + "\t" + str(k_counter))


if __name__ == "__main__":
    main()
