# Please Build file for Spark code samples written in Python.
# Author: Andrew Jarombek
# Date: 10/10/2022

filegroup(
    name = "python_files",
    srcs = glob(["*.py"]),
)

python_library(
    name = "da_spark_prototypes",
    srcs = ["da_spark_prototypes/main.py"],
    deps = [":pyspark", ":py4j"]
)

python_test(
    name = "test",
    srcs = ["da_spark_prototypes/test/test_main.py"],
    data = ["//Spark/data:generate_data_files"],
    deps = [":da_spark_prototypes"],
    labels = ["python_test"],
    test_runner = "pytest"
)

genrule(
    name = "test_cmd",
    cmd = ["pytest > pytest.log"],
    srcs = [":python_files", "//Spark/data:generate_data_files"],
    deps = [":pytest"],
    labels = ["python_test"],
    outs = ["pytest.log"]
)

pip_library(
    name = "pyspark",
    version = "3.3.0",
)

pip_library(
    name = "py4j",
    version = "0.10.9.5",
)

pip_library(
    name = "pytest",
    version = "7.1.3",
)

pip_library(
    name = "black",
    version = "22.10.0",
)