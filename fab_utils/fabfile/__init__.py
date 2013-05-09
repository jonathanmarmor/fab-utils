from fabric.api import env, task, sudo, run

import apt
import easy_install
import forever
import git
import npm
import pip
import upstart


# Fabric config
env.warn_only = True
env.user = 'ubuntu'


@task
def cmd(c, use_sudo=False):
    if use_sudo:
        sudo(c)
    else:
        run(c)
