#!/usr/bin/env python3

import sys, subprocess, re

url = sys.argv[1]

output = subprocess.run(f'wget -q -O- {url}', capture_output=True, text=True, shell=True)

numbers = re.findall(r'[\d -]+', output.stdout)

for num in numbers:
    num = re.sub(r'[ -]', '', num)
    
    if len(num) >= 8 and len(num) <= 15:
        print(num)