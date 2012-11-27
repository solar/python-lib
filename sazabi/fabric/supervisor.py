# vim: fileencoding=utf-8
"""
Supervisor utilities for fabric.
"""

from fabric.api import sudo

def supervisorctl(command, arg=''):
    sudo('supervisorctl {0} {1}'.format(command, arg))

def start(arg):
    supervisorctl('start', arg)

def restart(arg):
    supervisorctl('restart', arg)

def stop(arg):
    supervisorctl('stop', arg)

def status(arg=''):
    supervisorctl('status', arg)

def reread():
    supervisorctl('reread')

def update():
    supervisorctl('update')

def reload():
    supervisorctl('reload')

def add(arg):
    supervisorctl('add', arg)

def remove(arg):
    supervisorctl('remove', arg)

def update_program(program):
    supervisorctl('reread')
    supervisorctl('stop', program)
    supervisorctl('remove', program)
    supervisorctl('add', program)
