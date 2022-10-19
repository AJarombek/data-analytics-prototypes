#!/usr/bin/env bash

# Install dependencies for matplotlib code samples
# Author: Andrew Jarombek
# Date: 10/16/2022

lli "$1"/arithmetic.ll
printf "2 + 5 = %s \n" $?
