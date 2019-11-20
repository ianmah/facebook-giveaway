import requests
import json
import configparser
from random import shuffle, randint
import time
import pyfiglet

print('Gathering all entries...')

f = open("attendees.txt", "r", encoding="utf8")
text = f.read()
attendeeList = text.splitlines()

length = len(attendeeList)

print("Total entries:", length)
time.sleep(0.5)

def confirm_choice():
    while True:
        confirm = input('Would you like to redraw? [y]Yes or [n]No: ')
        if confirm in ('y', 'n'):
            if confirm is 'y':
                picker()
                return confirm
            else:
                print("\nCONGRATS.")
                return confirm
        else:
            print("\n[y]Yes or [n]No: ")

def picker():
    print("Generating a random number from 1 to", length)
    time.sleep(1)

    x = 0
    for z in range(200):
        x = randint(1, length)
        print(x, "    ",  end="\r")
        time.sleep(.015)

    time.sleep(2)
    print(x)

    strin = " Person in position " + str(x)
    for z in range(5):
        print(strin,  end="\r")
        strin += "."
        time.sleep(0.2)

    print("Person in position", x)
    ascii_banner = pyfiglet.figlet_format(attendeeList[x])
    print(ascii_banner)
    confirm_choice()

picker()