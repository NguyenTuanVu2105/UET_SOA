import os
import time 

while True:
    with open(os.path.join(os.getcwd(), 'Test/a.txt'), 'a') as f:
        f.write('hello')
    time.sleep(2)