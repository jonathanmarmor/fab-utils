# fab-utils

Fabric tasks for executing common commands on remote servers.

## Installation

    git clone https://github.com/exfm/fab_utils
    cd fab_utils
    python setup.py install

## Usage: From the command line

    cd fab_utils/fab_utils
    fab -H <hostname> apt.add_repository:ppa:chris-lea/node.js
    fab -H <hostname> apt.update
    fab -H <hostname> apt.install:nodejs,npm

## Usage: Imported into another fabfile

    from fab_utils import apt

    @task
    def install_node():
        apt.add_repository('ppa:chris-lea/node.js')
        apt.update()
        apt.install([
            'nodejs',
            'npm'
        ])

## To Do

This is just a skeleton at this point.  Please add more common tasks to existing wrappers (apt.py, npm.py, git.py, etc) and add more wrappers of popular tools.
