import subprocess
import sys


if __name__ == '__main__':
    print('My input parameters:', sys.argv)
    x = subprocess.run(["python", "app1.py"], capture_output=True)
    print(x.stdout)
