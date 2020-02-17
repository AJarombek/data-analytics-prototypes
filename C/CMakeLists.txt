# Make the C project for matrices.
# Author: Andrew Jarombek
# Date: 2/15/2020

cmake_minimum_required(VERSION 3.9)
project(matrices)

set(CMAKE_C_STANDARD 11)

add_executable(matrices matrices.c)