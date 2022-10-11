# Please Build file for Spark data sources.
# Author: Andrew Jarombek
# Date: 10/10/2022

filegroup(
    name = "data_files",
    srcs = glob(["*.jsonnet"]),
)

genrule(
    name = "generate_data_files",
    cmd = ["jsonnet exercises.jsonnet > exercises.json"],
    labels = ["data_files"],
    outs = [glob(["*.json"])]
)