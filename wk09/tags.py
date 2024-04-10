#! /usr/bin/env python3

# fetch specified web page and count the HTML tags in them

import sys, subprocess, re
from collections import Counter

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <url>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]

    # Fetch HTML from url
    output = subprocess.run(['wget', '-q', '-O-', url], capture_output=True, text=True)

    # Get all tags
    tags = re.findall(r'<\s*(\w+)', output.stdout)
    
    counter = Counter(tags)
    # for tag in tags:
        # counter[tag] += 1

    # Print in alphabetical order
    for tag, count in sorted(counter.items()):
        print(tag, count)

if __name__ == "__main__":
    main()