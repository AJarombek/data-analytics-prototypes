# Please Build file for Numpy code samples written in Python.
# Author: Andrew Jarombek
# Date: 10/12/2022

path = package_name()

genrule(
    name = "numpy_first_steps",
    cmd = [f"python3 {path}/numpy_first_steps.py > numpy_first_steps.log"],
    srcs = ["numpy_first_steps.py", "install_dependencies.sh"],
    labels = ["numpy"],
    outs = ["numpy_first_steps.log"]
)

genrule(
    name = "numpy_next_steps",
    cmd = [f"python3 {path}/numpy_next_steps.py > numpy_next_steps.log"],
    srcs = ["numpy_next_steps.py", "install_dependencies.sh"],
    labels = ["numpy"],
    outs = ["numpy_next_steps.log"]
)

genrule(
    name = "numpy_advanced",
    cmd = [f"python3 {path}/numpy_advanced.py > numpy_advanced.log"],
    srcs = ["numpy_advanced.py", "install_dependencies.sh"],
    labels = ["numpy"],
    outs = ["numpy_advanced.log"]
)

genrule(
    name = "numba_basics",
    cmd = [f". {path}/install_dependencies.sh && python3 {path}/numba_basics.py > numba_basics.log"],
    srcs = ["numba_basics.py", "install_dependencies.sh"],
    labels = ["numpy"],
    outs = ["numba_basics.log"]
)