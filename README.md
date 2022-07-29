# HCA Staging Import Validator

Runs a pre-check of a staging area to identify issues that might cause the snapshot or indexing processes to fail.

## Testing
NB - this can take over 10 hours to run, depending on the size of the staging area. In the future, we may want to add a fake test staging area to speed up testing.
```bash
python validate_staging_area.py --staging-area <gs_path> --ignore-dangling-inputs
```

## PRs
Once you have tested locally, built and pushed to TestPyPi successfully, you can submit a PR. Current reviewers are `aherbst-broad` and `danielsotirhos`.

## Building and publishing

We follow the basic python packaging and distribution [guide](https://packaging.python.org/tutorials/packaging-projects/).
These instructions assume you are working from the repository root, and that you have appropriate permissions to the
corresponding pypi project. It's encouraged that any changes to this package be tested via [testpypi](https://test.pypi.org) first.
(NB you will need accounts on both PyPI and test.pypi.org, as well as permission to upload to this project in both.)

>**⚠ WARNING:**
>Be sure to update the version number in the `pyproject.toml` file before building and uploading to (test)PyPI!<br>

* Install `build`:
```bash
python -m pip install --upgrade build
```
* Build packages:
```bash
python -m build
```
* Install `twine`:
```bash
python -m pip install --upgrade twine
```
* Test the upload:
```bash
python -m twine upload --repository testpypi dist/*
```
* Upload the package to pypi (ideally using an [API token](https://pypi.org/help/#apitoken))
```bash
python -m twine upload dist/*
```
