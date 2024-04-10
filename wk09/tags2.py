#! /usr/bin/env python3

# fetch specified web page and count the HTML tags in them

import sys, subprocess, re
from collections import Counter
from argparse import ArgumentParser

def main():
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument('-f', '--frequency', action='store_true', help='print tags by frequency')
    parser.add_argument('url', help='url to fetch')
    args = parser.parse_args()

    # Fetch HTML from url
    url = args.url
    output = subprocess.run(['wget', '-q', '-O-', url], capture_output=True, text=True)

    # Find tags
    tags = re.findall(r'<\s*(\w+)', output.stdout)
    
    counter = Counter(tags)

    if args.frequency:
        # Print in ascending order of frequency
        for tag, count in reversed(counter.most_common()):
            print(tag, count)
    else:
        # Print in alphabetical order
        for tag, count in sorted(counter.items()):
            print(tag, count)

if __name__ == "__main__":
    main()