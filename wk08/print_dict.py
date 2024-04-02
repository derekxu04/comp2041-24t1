#!/usr/bin/env python3

d = {
    'key': 'value',
    'Andrew': 'green',
    'Anne': 'red',
    'John': 'blue',
}

def print_dict(d):
    # for x in d.items():
    #     print(f"[{x[0]}] => {x[1]}")

    for key, value in d.items():
        print(f"[{key}] => {value}")

    # for key in d.keys():
    #     print(key, d[key])


print_dict(d)