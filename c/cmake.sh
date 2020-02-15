#!/usr/bin/env bash

# Commands for compiling and executing C code with CMake.
# Author: Andrew Jarombek
# Date: 2/15/2020

rm -rf build
mkdir build
cd build
cmake ..
make

./matrices