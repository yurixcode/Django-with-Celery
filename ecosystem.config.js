module.exports = {
    apps : [{
      name: 'worker',
      cmd: 'celery -A celeryapp worker -l info',
      autorestart: true,
      watch: true,
      instances: 4
    }]
  };