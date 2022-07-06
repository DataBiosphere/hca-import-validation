# HCA Staging Import Validator

Runs a pre-check of a staging area to identify issues that might cause the
snapshot or indexing processes to fail.

## Testing
```
python validate_staging_area.py --staging-area <gs_path> --ignore-dangling-inputs
```

## PRs
Once you have tested locally, built and pushed to TestPyPi successfully, you can submit a PR. Current reviewers are `aherbst-broad` and `danielsotirhos`.

## Building and publishing

We follow the basic python packaging and distribution [guide](https://packaging.python.org/tutorials/packaging-projects/).
These instructions assume you are working from the repository root, and that you have appropriate permissions to the 
corresponding pypi project. It's encouraged that any changes to this package be tested via [testpypi](https://test.pypi.org) first.
(NB you will need accounts on both PyPI and test.pypi.org, as well as permission to upload to this project in both.)

>   **⚠ WARNING:**
>   Be sure to update the version number in the `setup.cfg` file before uploading to PyPI!<br>
>   **⚠ AND once that is done:** make sure to update the version number in hca-ingest orchestration [pyproject.toml](https://github.com/DataBiosphere/hca-ingest/blob/1dd2669cf072d7a267a5f601bbd07a1d20eea040/orchestration/pyproject.toml#L25) file.

* Install `build`: 
```
python -m pip install --upgrade build
```
* Build packages:
```
python -m build
```
* Install `twine`:
```
python -m pip install --upgrade twine
```
* To first test the upload
```
python -m twine upload --repository testpypi dist/*
```
* Upload the package to pypi (ideally using an [API token](https://pypi.org/help/#apitoken))
```
python -m twine upload dist/*
```
