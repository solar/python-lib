# vim: fileencoding=utf-8
"""
Utilities for fabric.
"""

from os.path import basename, join

from string import Template
from StringIO import StringIO

from fabric.api import put, sudo
from fabric.colors import blue, yellow
from fabric.contrib import console, files

def symlink(from_file, target_dir, target_name=''):
    """
    Create symbolic link
    """
    if not files.exists(target_dir):
        puts(yellow('Target directory to link does not exist'))
        return

    if target_name:
        target = join(target_dir, target_name)
    else:
        target = join(target_dir, basename(from_file))

    if files.exists(target):
        if console.confirm(blue(target) + yellow(' already exists, '
                'are you sure you want to delete?')):
            sudo('rm -f {0}'.format(target))
        else:
            return

    sudo('ln -s {0} {1}'.format(from_file, target))

def upload_template(filename, destination, context, mode=None):
    """
    Create file from string.Template and upload it.
    """
    with open(filename) as f:
        tpl = Template(f.read())
    put(local_path=StringIO(tpl.substitute(context)),
            remote_path=destination,
            mode=mode)
