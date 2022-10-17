#!/usr/bin/env bash

# Install dependencies for matplotlib code samples
# Author: Andrew Jarombek
# Date: 10/16/2022

python3 -V
pip3 -V

if [ $? != 0 ]; then
  python3 -m ensurepip --upgrade
else
  printf "pip already installed.\n"
fi

python3 -c "import matplotlib"

if [ $? == 1 ]; then
    pip3 install matplotlib
else
    printf "matplotlib already installed.\n"
fi

python -c "import seaborn"

if [ $? == 1 ]; then
    pip3 install seaborn
else
    printf "seaborn already installed.\n"
fi
