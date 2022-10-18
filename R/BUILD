# Please Build file for R programming language code samples.
# Author: Andrew Jarombek
# Date: 10/17/2022

path = package_name()

genrule(
    name = "r_version",
    cmd = [f"Rscript --version > r.log"],
    labels = ["r"],
    outs = ["r.log"]
)

genrule(
    name = "r_basics",
    cmd = [f"Rscript {path}/basics.r > r_basics.log"],
    srcs = ["basics.r"],
    labels = ["r"],
    outs = ["r_basics.log"]
)