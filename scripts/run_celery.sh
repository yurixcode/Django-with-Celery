#!/bin/bash

echo "Starting Celery worker"
# celery -A celeryapp worker -l info
# pm2 start --no-daemon ecosystem.config.js
pm2-runtime ecosystem.config.js