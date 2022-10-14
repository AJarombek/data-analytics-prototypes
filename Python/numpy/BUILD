# Please Build file for Numpy code samples written in Python.
# Author: Andrew Jarombek
# Date: 10/12/2022

genrule(
    name = "numpy_first_steps",
    cmd = ["python3 Python/numpy/numpy_first_steps.py > numpy_first_steps.log"],
    srcs = ["numpy_first_steps.py"],
    labels = ["numpy"],
    outs = ["numpy_first_steps.log"]
)

genrule(
    name = "numpy_next_steps",
    cmd = ["python3 Python/numpy/numpy_next_steps.py > numpy_next_steps.log"],
    srcs = ["numpy_next_steps.py"],
    labels = ["numpy"],
    outs = ["numpy_next_steps.log"]
)

genrule(
    name = "numpy_advanced",
    cmd = ["python3 Python/numpy/numpy_advanced.py > numpy_advanced.log"],
    srcs = ["numpy_advanced.py"],
    labels = ["python_test"],
    outs = ["numpy_advanced.log"]
)