#! /usr/bin/env dash

#
# ==============================================================================
# test00.sh
# Test the pushy-add command.
#
# Written by: Derek Xu <derek.xu@student.unsw.edu.au>
# Date: 2024-03-12
# For COMP2041/9044 Assignment 1
# =========================================================================

# Colours
RED='\033[0;31m'
GREEN='\033[0;32m'

# add the current directory to the PATH so scripts
# can still be executed from it after we cd

PATH="$PATH:$(pwd)"

# Create a temporary directory for the test.
test_dir="$(mktemp -d)"
cd "$test_dir" || exit 1

# Create some files to hold output.

expected_output="$(mktemp)"
actual_output="$(mktemp)"

# Remove the temporary directory when the test is done.

trap 'rm "$expected_output" "$actual_output" -rf "$test_dir"' INT HUP QUIT TERM EXIT

# Create pushy repository

cat > "$expected_output" <<EOF
Initialized empty pushy repository in .pushy
EOF

pushy-init > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "${RED}Failed test"
    exit 1
fi

# Try to create another pushy repository

cat > "$expected_output" <<EOF
pushy-init: error: .pushy already exists
EOF
pushy-init > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "${RED}Failed test"
    exit 1
fi

# If passed test
echo "${GREEN}Test passed"
exit 0