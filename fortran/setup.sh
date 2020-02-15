#!/usr/bin/env bash

# Setup for working with Fortran on MacOS.
# Author: Andrew Jarombek
# Date: 2/15/2020

# https://github.com/fxcoudert/gfortran-for-macOS/releases
gfortran --version

# Execute Fortran code directly with the gfortran compiler
gfortran -o hello_world hello_world.f90
./hello_world

# Execute Fortran code with CMake
/bin/bash cmake.sh