#!/usr/bin/env bash

# Install dependencies for numpy code samples
# Author: Andrew Jarombek
# Date: 10/15/2022

python3 -V
pip3 -V

if [ $? != 0 ]; then
  python3 -m ensurepip --upgrade
else
  printf "pip already installed.\n"
fi

python3 -c "import numpy"

if [ $? == 1 ]; then
    pip3 install numpy
else
    printf "numpy already installed.\n"
fi

python -c "import numba"

if [ $? == 1 ]; then
    pip3 install numba
else
    printf "numba already installed.\n"
fi
