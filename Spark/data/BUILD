# Please Build file for Spark data sources.
# Author: Andrew Jarombek
# Date: 10/10/2022

filegroup(
    name = "data_files",
    srcs = glob(["*.jsonnet"]),
)

genrule(
    name = "generate_data_files",
    cmd = ["jsonnet Spark/data/exercises.jsonnet > exercises.json"],
    srcs = [":data_files"],
    labels = ["data_files"],
    outs = ["exercises.json"],
    visibility=["PUBLIC"]
)