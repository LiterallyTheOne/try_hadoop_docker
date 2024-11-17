"""reducer

0  | 1        | 2   | 3        | 4      | 5     | 6    | 7       | 8        | 9
id | uploader | age | category | length | views | rate | ratings | comments | related_ids


"""

from __future__ import print_function
import sys


def main():
    """main function"""
    c_id = None
    u_id = None
    counter = 0

    for x in sys.stdin:
        # x = x.replace("\n", "")
        x = x.strip()

        if x == "":
            continue

        y = x.split("\t")

        if len(y) < 9:
            continue

        print(y[3], sep="\t")

    #     if c_id != y[3] or u_id != y[0]:
    #         if c_id and u_id:
    #             print(c_id + "\t" + str(counter))
    #         counter = 0
    #         c_id = y[3]
    #         u_id = y[0]

    #     counter += 1

    # if c_id and u_id:
    #     print(c_id + "\t" + str(counter))


if __name__ == "__main__":
    main()
