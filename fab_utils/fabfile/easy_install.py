from fabric.api import task, sudo


@task
def easy_install(packages):
    if isinstance(packages, str):
        packages = [packages]

    sudo('easy_install {}'.format(' '.join(packages)))
