#!/bin/bash

echo "Starting Celery worker"
celery -A celeryapp worker -l info