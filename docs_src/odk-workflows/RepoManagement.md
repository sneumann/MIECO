# Manage your ODK Repository

This document describes how to keep your ODK repository up-to-date.

## Updating the ODK

From time to time, the ODK is updated with new features and bug fixes. To update your repository:

1. Check the [ODK CHANGELOG](https://github.com/INCATools/ontology-development-kit/blob/master/CHANGELOG.md) for updates
2. Update the ODK version in `src/ontology/mieco-odk.yaml` if needed
3. Run the repository update:

```bash
cd src/ontology
./run.sh make update_repo
```

4. Review the changes and commit them:

```bash
git add -A
git commit -m "Update ODK to vX.Y.Z"
git push origin master
```

## ODK Version

The current ODK version used in this repository is specified in:
- `.github/workflows/qc.yml` (container image version)
- `src/ontology/Makefile` (`ODK_VERSION_MAKEFILE` variable)

For more information, see: https://oboacademy.github.io/obook/howto/odk-update/
