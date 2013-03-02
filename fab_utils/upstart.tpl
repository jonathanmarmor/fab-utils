description "run {{service_name}} service"

version "1.0"

emits {{service_name}}_starting
emits {{service_name}}_running

# configuration variables.
env NODE_ENV={{node_env}}
env service_name={{service_name}}
env SERVICE_HOME=/home/ubuntu/apps/{{service_name}}

respawn
respawn limit 10 5

pre-start script
    chdir $SERVICE_HOME
    exec /usr/bin/npm install
    emit {{service_name}}_starting
end script

script
    chdir $SERVICE_HOME
    exec /usr/bin/npm start >> /home/ubuntu/apps/{{service_name}}/logs/upstart.log 2>&1
    emit {{service_name}}_running
end script
