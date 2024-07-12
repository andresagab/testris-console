import os
import time
from variables import *

def update():
    print("+" + "-" * 10 + "+")
    print("TETRIS-CONSOLE")
    time.sleep(udpate_time)
    os.system('"cls"')

if __name__ == "__main__":
    while True:
        update()