#! /bin/dash

mlalias cs2041.wed09-brass | 
sed -n '/Addresses/,/Owners/p' | 
head -n -1 |
tail -n +2 |
head -5 |
cut -d'@' -f1 | 
sed -E 's/^\s*//' |
while read zid; do
    acc "$zid" |  
    sed -n '/^$/,/^$/p' | 
    cut -d':' -f2 | 
    sed -En 's/^.*([A-Z]{4}[0-9]{4})t[0-3]_Student.*$/\1/p'
done |
sort | 
uniq -c |
sort -rn
