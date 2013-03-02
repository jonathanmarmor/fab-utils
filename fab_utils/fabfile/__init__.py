from fabric.api import env

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
