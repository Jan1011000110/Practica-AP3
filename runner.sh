#!/bin/bash

# Compile the C++ checker
g++ checker.cc -o checker

# Loop over numbers 1 to 10
for i in {1..10}; do
    # Run Python script and redirect input/output
    python3 exh.py out.txt < "med-$i.txt"

    # Run the compiled checker
    ./checker "med-$i.txt" out.txt
done
