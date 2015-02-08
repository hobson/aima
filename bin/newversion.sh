#!/usr/bin/env bash
# tells pypi to update the latest default version in the repo

# TODO: increment the version in __init__.py and add a tag to github with that version
# TODO: do it all in python (no bash)!
python setup.py register -r pypi
python setup.py sdist upload -r pypi