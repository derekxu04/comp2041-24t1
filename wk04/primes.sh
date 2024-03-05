#! /bin/dash

# Print prime numbers less than the specified argument

limit=$1

# Check i from 1 to limit - 1 if it's prime
#   -> if prime: echo
#   -> not prime: do nothing

i=1
while [ "$i" -lt "$limit" ]; do
    if ./is_prime.sh "$i" > /dev/null; then
        echo "$i"
    fi

    i=$((i + 1))
done