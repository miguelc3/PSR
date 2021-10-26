#!/usr/bin/python3

from colorama import Fore,  Back, Style
import argparse

def isPrime(value):
    print("\nReference Number " + str(value))

    for i in range(2, value):
        reminder = value % i
        print(str(value) + "/" + str(i) + " has reminder " + str(reminder))

        if reminder == 0:
            return False

    return True

def main():

    parse = argparse.ArgumentParser(description='PSR argparse example.')
    parse.add_argument('--max_number', type=int, help='Maximum number to search for primes')
    parse.add_argument('--verbose', action='store_true', help='Print something to the screen or not')
    args = vars(parse.parse_args())

    print("Start to compute prime numbers up to: " + str(args['max_number']))

    counter = 0
    for i in range(1, args['max_number']):
        if isPrime(i):
            counter +=1
            print(Fore.RED + Back.YELLOW + Style.BRIGHT + "Number " + Fore.LIGHTMAGENTA_EX + Back.CYAN + Style.DIM + str(i) + Fore.RED + Back.YELLOW + Style.BRIGHT + " is prime." + Style.RESET_ALL)
        else:
            print("Number " + str(i) + " is not prime")

    if args['verbose']:
        print(Fore.BLUE + "There are " + str(counter) + ' prime numbers between 1 and ' + str(args['max_number']) + Style.RESET_ALL)



if __name__ == "__main__":
    main()