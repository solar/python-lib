# vim: fileencoding=utf-8
"""
Utilities for sbt.
"""

from fabric.api import abort, local, puts
from fabric.colors import blue, red, yellow

import re

def version(pattern='\d+\.\d+(?:-.*)?'):
    out = local('sbt -no-colors version', capture=True)
    puts(out)
    pat = '^\[info\]\s+({0})$'.format(pattern)
    puts(pattern)
    matched = re.search('^\[info\]\s+({0})$'.format(pattern), out, re.M)

    if not matched:
        abort(red('Failed to get version'))
    version = matched.group(1)
    puts(yellow('version: ') + blue(version))
    return version

def assembly_jar_name(pattern):
    out = local('sbt -no-colors "*:assembly::assembly-jar-name"', capture=True)
    matched = re.search('^\[info\]\s+({0})$'.format(pattern), out, re.M)

    if not matched:
        abort(red('Failed to fetch jar-name'))
    jar_name = matched.group(1)
    puts(yellow('jar-name: ') + blue(jar_name))
    return jar_name
