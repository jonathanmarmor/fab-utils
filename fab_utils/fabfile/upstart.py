from fabric.api import task, run, sudo, execute
from fabric.contrib.files import upload_template


@task
def start(service_name):
    sudo('initctl start {}'.format(service_name))


@task
def stop(service_name):
    sudo('initctl stop {}'.format(service_name))


@task
def restart(service_name):
    result = sudo('initctl restart {}'.format(service_name))
    if 'initctl: Unknown instance' in result:
        execute(start, service_name)


@task
def list():
    run('initctl list')


@task
def status(service_name):
    run('initctl status {}'.format(service_name))


@task
def upload_config(service_name, node_env):
    print '* Compiling and uploading upstart config file.'
    ctx = {
        'service_name': service_name,
        'node_env': node_env
    }
    dest = '/etc/init/{}.conf'.format(service_name)

    upload_template('upstart.tpl', dest, ctx, use_jinja=True,
        mirror_local_mode=True, use_sudo=True)

    sudo('chown -R root:root {}'.format(dest))
