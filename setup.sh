#!/usr/bin/env bash

# Commands to start a Jupyter server to work with notebooks.
# Author: Andrew Jarombek
# Date: 2/8/2020

pip3 install --upgrade pip

# Install and start Jupyter.
pip3 install jupyter
jupyter notebook

# Modules used in Jupyter notebooks.
pip3 install numpy