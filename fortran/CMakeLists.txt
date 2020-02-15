# Build Fortran code with CMake.
# Author: Andrew Jarombek
# Date: 2/15/2019

cmake_minimum_required(VERSION 3.9)
project(fortran)

enable_language(Fortran)

add_executable("hello_world" "hello_world.f90")
set_target_properties(hello_world PROPERTIES LINKER_LANGUAGE Fortran)