import sys
import time
import requests
import random

API_URL = 'http://localhost:8000/jobs/'
NSIM_DEFAULT = 20

def random_sleep():
    time.sleep(random.randint(1, 15))

def random_data():
    return {'argument': random.randint(0, 100)}

def launch_simulation():
    response = requests.post(url=API_URL, data=random_data())
    if response:
        print('New task launched: ', response.json()['url'])
    else:
        print('Error launching task')

def main(argv):
    nsim = int(argv[0]) if argv else NSIM_DEFAULT 
    for _ in range(nsim):
        launch_simulation()
        random_sleep()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))