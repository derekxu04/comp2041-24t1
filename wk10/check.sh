#!/bin/sh

cut -d' ' -f1 |
sort |
uniq -c |
grep -Ev '^\s*[12] ' |
sed -E 's/^\s*[0-9]+ //'
