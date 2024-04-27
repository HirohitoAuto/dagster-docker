# Dagster - Multi Pipeline on Docker Compose

## Overview

This repository contains an example of running multiple pipelines using Dagster on Docker Compose.

- **pipeline_dbt**  : jaffle_shop dbt project
- **pipeline_x** : simple python pipeline
- **pipeline_y** : simple python pipeline


## Getting Started
1. **Set mounting path**

    `pipeline_dbt/` will be mounted on container to get it easy to fix code. 
    
    Replace this path in [dagster.yaml](https://github.com/HirohitoAuto/dagster-docker/blob/main/dagster.yaml) with absolute path to `pipeline_dbt/` on your computer.
    ```yml
    ...
    run_launcher:
        ...
            volumes: 
                - /var/run/docker.sock:/var/run/docker.sock
                - /tmp/io_manager_storage:/tmp/io_manager_storage
                - /ABSOLUTE_PATH/dagster-docker/pipeline_dbt:/opt/dagster/app/pipeline_dbt  #  <--- change this path !!!!
    ```


2. **Start the Docker Compose environment:**

    ```shell
    make up
    ```

4. **Access the Dagster UI:**

    Open your web browser and navigate to [http://localhost:3000](http://localhost:3000).

5. **Stop & Clean:**
    ```bash
    make down   # stop
    make clean  # clean
    ```

## Documentation
This project is based on official example code. For more information, please refer to ...

- [Deploying Dagster to Docker](https://docs.dagster.io/deployment/guides/docker#example)
- [dagster-io/dagster/examples /deploy_docker/](https://github.com/dagster-io/dagster/tree/1.7.3/examples/deploy_docker)
