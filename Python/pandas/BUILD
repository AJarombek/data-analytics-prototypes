# Please Build file for pandas code samples written in Python.
# Author: Andrew Jarombek
# Date: 10/16/2022

path = package_name()

genrule(
    name = "pandas_first_steps",
    cmd = [f"python3 {path}/pandas-first-steps.py > pandas-first-steps.log"],
    srcs = ["pandas-first-steps.py", "install_dependencies.sh"],
    labels = ["pandas"],
    outs = ["pandas-first-steps.log"]
)

genrule(
    name = "pandas_next_steps",
    cmd = [f"python3 {path}/pandas-next-steps.py > pandas-next-steps.log"],
    srcs = ["pandas-next-steps.py", "install_dependencies.sh"],
    labels = ["pandas"],
    outs = ["pandas-next-steps.log"]
)

genrule(
    name = "pandas_group_by",
    cmd = [f"python3 {path}/pandas-group-by.py > pandas-group-by.log"],
    srcs = ["pandas-group-by.py", "install_dependencies.sh"],
    labels = ["pandas"],
    outs = ["pandas-group-by.log"]
)

genrule(
    name = "pandas_sqlite",
    cmd = [f"python3 {path}/pandas-sqlite.py > pandas-sqlite.log"],
    srcs = ["pandas-sqlite.py", "install_dependencies.sh"],
    labels = ["pandas"],
    outs = ["pandas-sqlite.log"]
)

genrule(
    name = "pandas_time_series",
    cmd = [f"python3 {path}/pandas-time-series.py > pandas-time-series.log"],
    srcs = ["pandas-time-series.py", "install_dependencies.sh"],
    labels = ["pandas"],
    outs = ["pandas-time-series.log"]
)