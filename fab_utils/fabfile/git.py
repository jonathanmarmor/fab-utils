from fabric.api import task, run, cd


@task
def clone(repo, user='jonathanmarmor', private=False):
    with cd('/home/ubuntu'):
        run('mkdir apps')

    with cd('/home/ubuntu/apps'):
        if private:
            # Only works with SSH forwarding at the moment
            run('git clone git@github.com:{}/{}.git'.format(user, repo))
        else:
            run('git clone https://github.com/{}/{}.git'.format(user, repo))


@task
def update(repo):
    with cd('/home/ubuntu/apps/{}'.format(repo)):
        run('git reset --hard')
        run('git pull')
