#!/usr/bin/env bash

# Run the arithmetic.ll LLVM code and print the result
# Author: Andrew Jarombek
# Date: 10/18/2022

lli "$1"/arithmetic.ll
printf "2 + 5 = %s \n" $?
