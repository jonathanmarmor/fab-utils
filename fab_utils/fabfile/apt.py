"""Fabric tasks for executing apt commands on remote servers.

Usage from the command line:

    cd fab_apt/fab_apt
    fab -H <hostname> apt.add_repository:ppa:chris-lea/node.js
    fab -H <hostname> apt.update
    fab -H <hostname> apt.install:nodejs,npm

Usage imported into another fabfile:

    from fab_apt import apt

    @task
    def install_node():
        apt.add_repository('ppa:chris-lea/node.js')
        apt.update()
        apt.install([
            'nodejs',
            'npm'
        ])

"""

from fabric.api import task, sudo
from fabric.contrib.files import append


@task
def install(packages):
    if isinstance(packages, str):
        packages = [packages]

    sudo('DEBIAN_FRONTEND=noninteractive apt-get install -y {}'.format(
        ' '.join(packages)))


@task
def add_repository(name):
    sudo('add-apt-repository {}'.format(name))


@task
def update():
    sudo('apt-get update')


@task
def add_source(source):
    append('/etc/apt/sources.list', source, use_sudo=True)


# @todo Add key
