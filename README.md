# HCA Staging Import Validator

Runs a pre-check of a staging area to identify issues that might cause the
snapshot or indexing processes to fail.

## Building and publishing

We follow the basic python packaging and distribution [guide](https://packaging.python.org/tutorials/packaging-projects/).
These instructions assume you are working from the repository root, and that you have appropriate permissions to the 
corresponding pypi project. It's encouraged that any changes to this package be tested via [testpypi](https://test.pypi.org) first.

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
* Upload the package to pypi (ideally using an [API token](https://pypi.org/help/#apitoken))
```
python -m twine upload dist/*
```
