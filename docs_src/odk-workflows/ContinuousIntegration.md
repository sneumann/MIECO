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

Automatically rebuilds the MkDocs site and commits the generated HTML to `docs/`
on every push to master. GitHub Pages is then configured to serve from that
`docs/` folder — no separate `gh-pages` branch required.

This is intentionally simpler than using a third-party action such as
`mhausenblas/mkdocs-deploy-gh-pages` because:

- It has no external action dependency (the `mhausenblas` action is unpinned and
  could change or disappear).
- There is no `gh-pages` branch to manage — everything lives on `master`.
- GitHub Pages setup is a single repository setting: *serve from `/docs` on master*.
- The generated HTML is visible directly in the repository.
- Documentation can also be updated entirely without CI: run `mkdocs build`
  locally and commit the `docs/` output.

## Viewing CI Results

Check the [Actions tab](https://github.com/sneumann/MIECO/actions) to see CI results.

For more information, see: https://oboacademy.github.io/obook/howto/odk-workflows/
