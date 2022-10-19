# data-analytics-prototypes

![Maintained Label](https://img.shields.io/badge/Maintained-Partially-yellow?style=for-the-badge)

### Overview

Prototypes / Code Samples for Data Analytics concepts and code libraries.  The following languages are explored in this 
repository:

> Python - Numpy, Pandas, Matplotlib libraries are among the most popular in data analytics.

> C - Many data analytics libraries use C at a lower-level or are based on C concepts.

> Fortran - Fortran still has a niche audience in the data analytics world.

> LLVM - LLVM is used by some data analytic libraries to compile higher-level code to machine code.

> R - R is the best option if you need a domain-specific language for data analytics.

### Commands

**Local Please Build Commands**

```bash
# Python/numpy
plz build //Python/numpy:numpy_first_steps -vvv
cat plz-out/gen/Python/numpy/numpy_first_steps.log

plz build //Python/numpy:numpy_next_steps -vvv
cat plz-out/gen/Python/numpy/numpy_next_steps.log

plz build //Python/numpy:numpy_advanced -vvv
cat plz-out/gen/Python/numpy/numpy_advanced.log

plz build //Python/numpy:numba_basics -vvv
cat plz-out/gen/Python/numpy/numba_basics.log

# Python/matplotlib
plz build //Python/matplotlib:matplotlib_first_steps -vvv

# Python/pandas
plz build //Python/... -i pandas -vvv
 
# R
plz build //R:r_version -vvv
plz build //R:r_basics -vvv
```

**Install Please Build**

```bash
curl https://get.please.build | bash
source ~/.profile
plz --version
```

**Create Python Docker Image**

```bash
docker login --username=ajarombek
docker image build -t data-analytics-prototypes-python:latest ./Python

# Push image to DockerHub with tag 'latest'
docker image tag data-analytics-prototypes-python:latest ajarombek/data-analytics-prototypes-python:latest
docker push ajarombek/data-analytics-prototypes-python:latest
```

**Create R Docker Image**

```bash
docker login --username=ajarombek
docker image build -t data-analytics-prototypes-r:latest ./R

# Push image to DockerHub with tag 'latest'
docker image tag data-analytics-prototypes-r:latest ajarombek/data-analytics-prototypes-r:latest
docker push ajarombek/data-analytics-prototypes-r:latest
```

### Directories

| Directory Name    | Description                                                                                              |
|-------------------|----------------------------------------------------------------------------------------------------------|
| `.github`         | GitHub Actions for CI/CD pipelines.                                                                      |
| `.run`            | Run configurations to use in PyCharm/IntelliJ IDEs.                                                      |
| `Airflow`         | Code samples for Airflow, which contains DAG files written in Python but otherwise is language agnostic. |
| `C`               | Code samples / prototypes written in C.                                                                  |
| `Fortran`         | Code samples / prototypes written in Fortran.                                                            |
| `LLVM`            | Code samples / prototypes written in LLVM.                                                               |
| `Python`          | Code samples / prototypes written in Python.                                                             |
| `R`               | Code samples / prototypes written in R.                                                                  |
| `Spark`           | Code samples for Spark, which are written in Python, Scala, SQL, and more.                               |
| `.plzconfig`      | Please Build configuration file for the repository.                                                      |
| `BUILD`           | Please Build rules for the top level directory of the repository.                                        |

### Version History

**[v1.0.0](https://github.com/AJarombek/data-analytics-prototypes/tree/v1.0.0) - Initial Version**

> Release Date: Jan 11th, 2022

* Initial data analytics code samples, mostly for Numpy, Pandas, and Airflow.
