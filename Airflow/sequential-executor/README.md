### Overview

Docker compose file for running Airflow with a sequential executor.

### Commands

**Docker Compose Setup**

```bash
# Start the server
docker system prune
docker-compose up

# Stop the server
docker-compose down
```

### Files

| Filename             | Description                                                                             |
|----------------------|-----------------------------------------------------------------------------------------|
| `docker-compose.yml` | Docker compose file for configuring an Airflow server.                                  |
| `Dockerfile`         | Dockerfile that prepares the Airflow image to use the sequential executor.              |
