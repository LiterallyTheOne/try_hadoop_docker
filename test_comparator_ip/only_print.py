"""Only print"""

from __future__ import print_function
import sys


def main():
    """main function"""

    for x in sys.stdin:
        x = x.replace("\n", "")

        print(x)


if __name__ == "__main__":
    main()
