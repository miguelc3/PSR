#!/usr/bin/python3
from colorama import Fore,  Back, Style

max_number = 8

def isPrime(value):
    print("\nReference Number " + str(value))

    for i in range(2, value):
        reminder = value % i
        print(str(value) + "/" + str(i) + " has reminder " + str(reminder))

        if reminder == 0:
            return False

    return True

def main():
    print("Start to compute prime numbers up to: " + str(max_number))

    counter = 0
    for i in range(1, max_number):
        if isPrime(i):
            counter +=1
            print(Fore.RED + Back.YELLOW + Style.BRIGHT + "Number " + str(i) + " is prime." + Style.RESET_ALL)
        else:
            print("Number " + str(i) + " is not prime")

    print(Fore.BLUE + "Total of prime numbers: " + str(counter) + Style.RESET_ALL)
    print("Back to normal now")


if __name__ == "__main__":
    main()


