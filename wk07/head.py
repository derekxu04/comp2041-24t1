#! /usr/bin/env python3

import sys

def head():
    n_lines = 10

    if len(sys.argv) > 1 and sys.argv[1].startswith('-'):
        arg = sys.argv[1]
        arg = arg[1:]
        n_lines = int(arg)

        sys.argv.pop(1)

    # Check if no files given
    if len(sys.argv) == 1:
        # Read from stdin
        i = 1
        for line in sys.stdin:
            print(line, end='')

            if i == n_lines:
                break

            i += 1
    else:
        for file in sys.argv[1:]:
            i = 1
            with open(file) as stream:
                for line in stream:
                    print(line, end='')

                    if i == n_lines:
                        break

                    i += 1
            
if __name__ == '__main__':
    head()
