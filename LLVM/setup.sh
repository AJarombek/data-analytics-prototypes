#!/usr/bin/env bash

# Commands to execute LLVM Intermediate Representation.
# Author: Andrew Jarombek
# Date: 2/17/2020

sudo chown -R $(whoami) /usr/local/Frameworks
chmod u+w /usr/local/Frameworks

brew install llvm

/usr/local/opt/llvm/bin/lli --version

/usr/local/opt/llvm/bin/lli helloworld.ll
/usr/local/opt/llvm/bin/lli basics.ll

/usr/local/opt/llvm/bin/lli arithmetic.ll

# Exit code from arithmetic.ll will be the result of 2 + 3
echo $?