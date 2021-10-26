#!/usr/bin/python3

'''
Miguel Pereira, nº88731
PSR 21/22
Part_2
Ex.4
'''

import readchar
from colorama import Fore, Back, Style

# a)
def printAllCharsUpTo(stop_char):
    # function ord gives the number of a giver character on the ascii table
    print('Printing all values from space to ' + str(stop_char))
    for i in range(ord(' '),ord(stop_char)+1):
        # function chr returns the character from an integer of the ascii table
        print(chr(i))

# b)
def readAllUpTo(stop_key):

    print('Type something (X to stop)')

    pressed_key = readchar.readkey()
    while pressed_key != stop_key:
        pressed_key = readchar.readkey()
        print('Thank you for typing ' + pressed_key )

    print('You pressed ' + stop_key + '. Terminating')

    # Another way to do the exercise is to use While true:
    '''
    while True:
        pressed_key = readchar.readkey()

        
        if pressed_key == stop_key:
            print('You typed ' + stop_key + '. Terminating.')
            break
        else:
            print('Thank you for typing ' + pressed_key )
    '''

# c)
def countNumbersUpTo(stop_key):
    print('Type something (X to stop)')

    tot_numbers = 0
    tot_others= 0

    while True:
        pressed_key = readchar.readkey()

        if pressed_key == stop_key:
            print('You typed ' + stop_key + '. Terminating.')
            break
        else:
            print('Thank you for typing ' + Fore.RED + Style.BRIGHT + pressed_key + Style.RESET_ALL)
            if pressed_key.isnumeric():
                tot_numbers +=1
            else:
                tot_others +=1

    print('You pressed ' + Fore.BLUE + Style.BRIGHT + str(tot_numbers) + Style.RESET_ALL + ' numbers')
    print('You pressed ' + Fore.BLUE + Style.BRIGHT + str(tot_others) + Style.RESET_ALL + ' others')

def main():

    # a)
    # print('Give me the stop char: ')
    # pressed_char = readchar.readchar()
    # printAllCharsUpTo(pressed_char)

    # b)
    # readAllUpTo('X')

    # c)
    # countNumbersUpTo('X')

if __name__ == '__main__':
    main()