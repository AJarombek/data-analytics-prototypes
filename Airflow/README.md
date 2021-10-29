### Overview

Code samples for working with Airflow.

### Commands

**Initial Setup**

```bash
# Start the server
docker system prune
docker-compose up

# Stop the server
docker-compose down
```

**Local Coding Environment Setup**

```bash
# One time Poetry install
pip3 install poetry
poetry env info

# Start the virtual environment and install the dependencies
poetry shell
poetry install
```

### Files

| Filename             | Description                                                                             |
|----------------------|-----------------------------------------------------------------------------------------|
| `docker-compose.yml` | Docker compose file for configuring an Airflow server.                                  |
| `poetry.lock`        | Lock file containing Python dependencies installed by Poetry.                           |
| `pyproject.toml`     | [Poetry](https://python-poetry.org/) dependency management configuration file.          |
| `dags`               | Directory holding Python DAG files.                                                     |