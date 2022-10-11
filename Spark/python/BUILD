# Please Build file for Spark code samples written in Python.
# Author: Andrew Jarombek
# Date: 10/10/2022

filegroup(
    name = "python_files",
    srcs = glob(["*.py"]),
)

python_test(
    name = "test",
    srcs = [":python_files"],
    deps = ["//Spark/data:generate_data_files"],
    labels = ["python_test"],
    test_runner = "pytest"
)