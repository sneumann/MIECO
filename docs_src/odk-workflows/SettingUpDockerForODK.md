# Setting up Docker for ODK

This document describes how to set up Docker for use with the ODK.

## Installation

1. Install Docker Desktop for your platform:
   - [Mac](https://docs.docker.com/desktop/install/mac-install/)
   - [Windows](https://docs.docker.com/desktop/install/windows-install/)
   - [Linux](https://docs.docker.com/desktop/install/linux-install/)

2. Verify Docker is working:

```bash
docker run hello-world
```

## Pulling the ODK Image

Pull the ODK Docker image:

```bash
docker pull obolibrary/odkfull:v1.5.4
```

## Using run.sh

The `run.sh` script in `src/ontology/` wraps Docker commands for you:

```bash
cd src/ontology
./run.sh make test
```

For more information, see: https://oboacademy.github.io/obook/howto/odk-setup/
