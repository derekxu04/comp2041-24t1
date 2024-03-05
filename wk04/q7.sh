#! /bin/dash

acc z5419252 |  
sed -n '/^$/,/^$/p' | 
cut -d':' -f2 | 
sed -En 's/^.*([A-Z]{4}[0-9]{4})t[0-3]_Student.*$/\1/p'