#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.context_managers import lcd
from fabric.api import local, run, env, cd, put

env.hosts = ['webuser@10.0.0.192:22']
env.passwords = {'webuser@10.0.0.192:22': 'password'}
LOCAL_SRC = '/tmp'


def remote():
    print '----- remote -----'
    local('uname -mrs')
    local('free -m')

    with lcd(LOCAL_SRC):
        local('touch /tmp/a.txt')
        local('test -f /tmp/a.txt', capture=False)
        out = local('md5sum /tmp/a.txt', capture=True)
        print out
        print out[0:32]
        # like scp
        put('/tmp/a.txt', '/tmp/b.txt')
        out2 = run('md5sum /tmp/b.txt')
        print out2

    run('uname -mrs')
    run('free -m')
    cd('/tmp')
    run('pwd')

