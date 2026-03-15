# Release Workflow

This document describes how to make a release of MIECO.

## Prerequisites

1. Install [Docker](https://www.docker.com/get-docker)
2. Ensure all changes are committed and pushed to master
3. Ensure the CI is passing

## Making a Release

1. Navigate to `src/ontology`
2. Run the release pipeline:

```bash
cd src/ontology
./run.sh make prepare_release
```

3. Review the generated release files in the repository root
4. Commit the release files:

```bash
git add mieco.owl mieco-base.owl
git commit -m "Release YYYY-MM-DD"
git push origin master
```

5. Create a release tag on GitHub:
   - Go to https://github.com/sneumann/MIECO/releases/new
   - Tag: `vYYYY-MM-DD`
   - Title: `YYYY-MM-DD`
   - Click "Publish release"

## Release Artefacts

The following release artefacts are generated:

- `mieco.owl` - The primary release file
- `mieco-base.owl` - The base release (no imported axioms)

For more information, see the [ODK release documentation](https://oboacademy.github.io/obook/reference/release-artefacts/).
