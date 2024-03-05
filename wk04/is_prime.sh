#! /bin/dash

# Tests whether the specified integer is a prime


number=$1

# Check all i from 2 to sqrt(number)
# if number is divisible by i
#   -> if divisible by any: not prime
#   -> if divisible by none: is prime

if [ "$number" -eq 1 ]; then
    echo "$number is not prime"
    exit 1
fi

i=2
while [ $((i * i)) -le "$number" ]; do
    
    # Check if number is divisible by i
    if [ $((number % i)) -eq 0 ]; then
        echo "$number is not prime"
        exit 1
    fi

    i=$((i + 1))
done

echo "$number is prime"
exit 0