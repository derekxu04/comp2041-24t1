#! /usr/bin/env python3

# fetch specified web page and count the HTML tags in them

import sys, subprocess, re, requests
from collections import Counter
from argparse import ArgumentParser
from bs4 import BeautifulSoup

def main():
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument('-f', '--frequency', action='store_true', help='print tags by frequency')
    parser.add_argument('url', help='url to fetch')
    args = parser.parse_args()

    # Fetch HTML from url
    url = args.url
    response = requests.get(url)

    soup = BeautifulSoup(response.text)

    tags = soup.find_all()

    counter = Counter([tag.name for tag in tags])

    if args.frequency:
        for tag, count in reversed(counter.most_common()):
            print(tag, count)
    else:
        for tag, count in sorted(counter.items()):
            print(tag, count)

if __name__ == "__main__":
    main()