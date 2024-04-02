#!/usr/bin/env python3

"""
count lines of Python source code
"""

from glob import glob

def main():
    for filename in glob("*.py"):
        with open(filename) as f:
            # Returns a list of all lines
            lines = f.readlines()

            print(f"{len(lines):7} {filename}")


if __name__ == "__main__":
    main()