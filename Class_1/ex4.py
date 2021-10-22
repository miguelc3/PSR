#!/usr/bin/python3
# chmod 777 ex4.py -> meter no terminal
from colorama import Fore,  Back, Style

# Perfect numbers

maximum_number = 10000

def getDividers(value):
    dividers = []

    for i in range(1, value):
        reminder = value % i
        # print(str(value) + "/" + str(i) + " has reminder " + str(reminder))

        if reminder == 0:
            dividers.append(i)

    #print('Dividers for ' + str(value) + ' are: ' + str(dividers) )
    return dividers


def isPerfect(value):

    dividers = getDividers(value)

    if sum(dividers) == value:
        return True

    return False


def main():

    print('Until ' + str(maximum_number) + ' these are the perfect numbers:')
    for i in range(1, maximum_number):
        if isPerfect(i):
            print(Fore.RED + 'Number ' + str(i) + ' is perfect.' + Style.RESET_ALL)



if __name__ == "__main__":
    main()
