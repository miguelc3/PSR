#!/usr/bin/python3
# for more information on time: https://www.programiz.com/python-programming/time

import time
import math
from colorama import Fore, Back, Style

def main():
    in_seconds = time.time()
    local_time = time.ctime(in_seconds)

    print('This is Ex1 and the local time is: ' +  Fore.BLUE + Back.YELLOW + Style.BRIGHT +
          local_time + Style.RESET_ALL)

    max_number = 50000000
    sqrts = []

    for i in range(1, max_number):
        number = math.sqrt(i)
        sqrts.append(number)

    final_seconds = time.time()
    elapsed_time = final_seconds - in_seconds
    print('Elapsed time: ' + str(elapsed_time))


if __name__ == '__main__':
    main()
