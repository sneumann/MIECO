These notes are for the EDITORS of mieco

For more details on ontology management, please see the OBO tutorial:

 * https://oboacademy.github.io/obook/

## Editors Version

The editors version is [mieco-edit.owl](mieco-edit.owl)

** DO NOT EDIT mieco.owl directly **

mieco.owl is the release version

The editors version can be edited using [Protégé](https://protege.stanford.edu/).

## Setting up Docker

The workflow relies on Docker. Please follow the instructions here:

 * https://oboacademy.github.io/obook/howto/odk-setup/

## Working with the Makefile

To run quality control tests locally (requires Docker):

```
cd src/ontology
./run.sh make test IMP=false PAT=false MIR=false
```

To prepare a release:

```
cd src/ontology
./run.sh make prepare_release
```

## ID Ranges

See the [mieco-idranges.owl](mieco-idranges.owl) file for ID range allocations.

## Git Quick Guide

After editing mieco-edit.owl:

1. Commit your changes: `git commit -m "description of change"`
2. Push to GitHub: `git push origin master`
3. CI will run automatically via GitHub Actions

## Release Manager notes

Releases are managed via GitHub Actions. To create a release:

1. Ensure all changes are merged to master
2. Run: `cd src/ontology && ./run.sh make prepare_release`
3. Commit the release files
4. Tag the release on GitHub

For more details, see:
 * https://oboacademy.github.io/obook/howto/odk-workflows/
