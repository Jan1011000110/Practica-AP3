#!/bin/bash

# Compile the C++ checker
g++ checker.cc -o checker

# Loop over numbers 1 to 10
for i in {1..10}; do
    # Run Python script and redirect input/output
    python3 exh.py out.txt < "public_benchs/easy-$i.txt"

    # Run the compiled checker
    ./checker "public_benchs/easy-$i.txt" out.txt
done
