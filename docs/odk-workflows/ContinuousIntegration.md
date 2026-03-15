# Continuous Integration

This document describes the CI pipeline for MIECO.

## Overview

MIECO uses GitHub Actions for continuous integration. The CI pipeline runs automatically on:
- Every push to the `master` branch
- Every pull request targeting the `master` branch

## Workflows

### QC Workflow (`.github/workflows/qc.yml`)

Runs ontology quality control checks using the ODK Docker container:

1. **Reasoning test**: Validates the ontology is consistent using the ELK reasoner
2. **SPARQL validation**: Runs SPARQL queries to check for common errors
3. **ROBOT report**: Generates a quality report

The CI runs with:
```
make test IMP=false PAT=false MIR=false
```

The `IMP=false`, `PAT=false`, and `MIR=false` flags skip import refreshing, pattern processing, and mirror refreshing for faster CI runs.

### Docs Workflow (`.github/workflows/docs.yml`)

Automatically builds and deploys documentation to GitHub Pages on every push to master.

## Viewing CI Results

Check the [Actions tab](https://github.com/sneumann/MIECO/actions) to see CI results.

For more information, see: https://oboacademy.github.io/obook/howto/odk-workflows/
