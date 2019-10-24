#!/bin/bash

echo "Starting Celery workers"

# From https://stackoverflow.com/questions/48646745/celery-multi-inside-docker-container

# safety switch, exit script if there's error. Full command of shortcut `set -e`
set -o errexit
# safety switch, uninitialized variables will stop script. Full command of shortcut `set -u`
set -o nounset

# tear down function
teardown()
{
    echo " Signal caught..."
    echo "Stopping celery multi gracefully..."

    # send shutdown signal to celery workser via `celery multi`
    # command must mirror some of `celery multi start` arguments
    celery -A celeryapp multi stop 3 --logfile=./logs/celery/worker-%n%I.log \
        --pidfile=/var/run/celery-%n.pid 
        
    echo "Stopped celery multi..."
    echo "Stopping last waited process"
    kill -s TERM "$child" 2> /dev/null
    echo "Stopped last waited process. Exiting..."
    exit 1
}

# start 3 celery worker via `celery multi` with declared logfile for `tail -f`
celery -A celeryapp multi start 3 -l INFO --logfile=./logs/celery/worker-%n%I.log \
    --pidfile=/var/run/celery-%n.pid 
    

# start trapping signals (docker sends `SIGTERM` for shudown)
trap teardown SIGINT SIGTERM

# tail all the logs continuously to console for `docker logs` to see
tail -f ./logs/celery/worker*.log &

# capture process id of `tail` for tear down
child=$!

# waits for `tail -f` indefinitely and allows external signals,
# including docker stop signals, to be captured by `trap`
wait "$child"