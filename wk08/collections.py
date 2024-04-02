#!/usr/bin/env python3

from collections import Counter, defaultdict, OrderedDict

# d = {}

# # Check if key already exists
# if 'a' in d.keys():
#     d['a'] += 1
# else:
#     d['a'] = 1
# d['a'] += 1
# d['b'] += 1
# d['a'] += 1
# print(d)

# c = Counter()

# c['a'] += 1
# c['b'] += 1
# c['a'] += 1

# print(c)

# print(c.most_common(1))

# initialises any unseen keys to a default value
# dd = defaultdict()

# print(dd['a'])
# dd['a'].append('bcde')
# dd['b'].append('hello')


# od = OrderedDict()

# od['z'] = 10
# od['a'] = 5
# od['b'] = 6

# print(od.keys())

c = Counter('hello world')
print(c)