#!/usr/bin/env python3

"""
print words in file 1 but not file 2
"""

import sys

# ./missing_words file1 file2

def main():
    if len(sys.argv) != 3:
        print('error')
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    words1 = set()
    with open(file1) as f1:
        for line in f1:
            words1.add(line.strip())

    words2 = set()
    with open(file2) as f2:
        for line in f2:
            words2.add(line.strip())

    # for word in words1:
    #     if word not in words2:
    #         print(word)
    
    for word in sorted(words1 - words2):
        print(word)



if __name__ == "__main__":
    main()