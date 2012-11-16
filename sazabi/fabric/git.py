# vim: fileencoding=utf-8
"""
Git utilities for fabric.
"""

from fabric.api import abort, local, quiet
from fabric.colors import red

def check_working_copy():
    """
    Check if working copy is clean.
    """
    with quiet():
        if local('git diff --quiet').failed:
            abort(red('Working copy is not clean'))

def checkout(commit):
    """
    Checkout specified commit.
    """
    check_working_copy()
    local('git checkout --quiet {0}'.format(commit))
