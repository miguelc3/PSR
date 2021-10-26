#!/usr/bin/python3

import readchar
from colorama import Fore, Back, Style

def countNumbersUpTo(stop_key):

    pressed_keys = [] # empty list to start with

    while True:

        print('Type something (X to stop)')
        pressed_key = readchar.readkey()

        if pressed_key == stop_key:
            print('You typed ' + stop_key + '. Terminating.')
            break
        else:
            print('Thank you for typing ' + Fore.RED + Style.BRIGHT + pressed_key + Style.RESET_ALL)
            pressed_keys.append(pressed_key)

    print('The keys you pressed are ' + Back.CYAN + str(pressed_keys) + Style.RESET_ALL)

    # Analyse the list and count
    tot_numbers = 0
    tot_others = 0
    pressed_numbers = []
    pressed_others = []
    dict_others = {}
    # counter = 0 # total of keys pressed - I used the enumerate instead

    # enumerate gives us not also acess to the list of, in this case, pressed_keys, but also to
    # the index in witch they were presses, so it isn't necessary to use a counter
    for idx_pressed_key, pressed_key in enumerate(pressed_keys):
        # counter += 1 # I used the enumerate instead
        if pressed_key.isnumeric():
            tot_numbers += 1
            pressed_numbers.append(pressed_key)
        else:
            tot_others += 1
            pressed_others.append(pressed_key)
            dict_others[idx_pressed_key] = pressed_key

    # if I use "set" the list ordered_numbers will not countaing any repeeated numbers
    ordered_numbers = list(set(pressed_numbers))
    ordered_numbers.sort() # sort is used to ordering the numbers of a list
    print('You pressed ' + Fore.BLUE + Style.BRIGHT + str(tot_numbers) + Style.RESET_ALL + ' numbers: ' + str(pressed_numbers))
    print('Pressed numberes ordered: ' + str(ordered_numbers))
    print('You pressed ' + Fore.BLUE + Style.BRIGHT + str(tot_others) + Style.RESET_ALL + ' others: ' + str(pressed_others))
    print('Dicionário de others: ' + str(dict_others))

    # Coloured text
    print('Colored text:')
    colors = [Fore.BLUE, Fore.CYAN, Fore.RED, Fore.YELLOW, Fore.LIGHTMAGENTA_EX, Fore.BLACK, Fore.GREEN]

    idx = 0
    text = ''
    for pressed_other in pressed_others:
        idx +=1
        text += colors[idx] + str(pressed_other) + Style.RESET_ALL
        if idx == len(colors)-1:
            idx = 0

    print(text)

    # List of numbers using list comprehension
    list_numbers = [x for x in pressed_keys if x.isnumeric()]
    print('List of numbers using list comprehension: ' + str(list_numbers))

def main():
    countNumbersUpTo('X')


if __name__ == "__main__":
    main()