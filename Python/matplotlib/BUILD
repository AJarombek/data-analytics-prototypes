# Please Build file for matplotlib code samples written in Python.
# Author: Andrew Jarombek
# Date: 10/16/2022

path = package_name()

genrule(
    name = "matplotlib_first_steps",
    cmd = [f"python3 {path}/matplotlib-first-steps.py > matplotlib-first-steps.log"],
    srcs = ["matplotlib-first-steps.py", "install_dependencies.sh"],
    labels = ["matplotlib"],
    outs = ["matplotlib-first-steps.log"]
)