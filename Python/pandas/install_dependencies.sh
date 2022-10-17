#!/usr/bin/env bash

# Install dependencies for pandas code samples
# Author: Andrew Jarombek
# Date: 10/16/2022

python3 -V
pip3 -V

if [ $? != 0 ]; then
  python3 -m ensurepip --upgrade
else
  printf "pip already installed.\n"
fi

python3 -c "import pandas"

if [ $? == 1 ]; then
    pip3 install pandas
else
    printf "pandas already installed.\n"
fi

python -c "import sqlalchemy"

if [ $? == 1 ]; then
    pip3 install sqlalchemy
else
    printf "sqlalchemy already installed.\n"
fi
