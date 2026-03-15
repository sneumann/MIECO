# Editors Workflow

This document describes how to edit the MIECO ontology.

## Prerequisites

1. Install [Docker](https://www.docker.com/get-docker)
2. Clone the repository: `git clone https://github.com/sneumann/MIECO`
3. Open a terminal and navigate to `src/ontology`

## Editing the Ontology

The source file to edit is `src/ontology/mieco-edit.owl`.

You can use [Protégé](https://protege.stanford.edu/) to edit the ontology.

## Running Quality Checks

After editing, run the quality checks locally using the ODK wrapper:

```bash
cd src/ontology
./run.sh make test IMP=false PAT=false MIR=false
```

## Committing Changes

After verifying your changes pass quality checks:

```bash
git add src/ontology/mieco-edit.owl
git commit -m "Brief description of change"
git push origin master
```

The CI pipeline will automatically run quality checks on your commits.

For more information, see the [ODK documentation](https://oboacademy.github.io/obook/howto/odk-workflows/).
