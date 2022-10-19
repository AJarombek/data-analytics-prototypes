# Please Build file for LLVM programming code samples.
# Author: Andrew Jarombek
# Date: 10/18/2022

path = package_name()

genrule(
    name = "llvm_version",
    cmd = ["lli --version > llvm.log"],
    labels = ["llvm"],
    outs = ["llvm.log"]
)

genrule(
    name = "llvm_hello_world",
    cmd = [f"lli {path}/helloworld.ll > llvm_hello_world.log"],
    srcs = ["helloworld.ll"],
    labels = ["llvm"],
    outs = ["llvm_hello_world.log"]
)

genrule(
    name = "llvm_basics",
    cmd = [f"lli {path}/basics.ll > llvm_basics.log"],
    srcs = ["basics.ll"],
    labels = ["llvm"],
    outs = ["llvm_basics.log"]
)

genrule(
    name = "llvm_arithmetic",
    cmd = [f"bash {path}/run_arithmetic.sh {path} > llvm_arithmetic.log"],
    srcs = ["arithmetic.ll", "run_arithmetic.sh"],
    labels = ["llvm"],
    outs = ["llvm_arithmetic.log"]
)