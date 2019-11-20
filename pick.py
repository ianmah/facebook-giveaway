import requests
import json
import facebook
import configparser
from random import shuffle, randint
import time
import pyfiglet

print('Gathering all entries...')

config = configparser.ConfigParser()
config.read('config.ini')

token = config['DEFAULT']['TOKEN']

graph = facebook.GraphAPI(access_token=token, version = 3.3)

# Smart TV Giveaway
data = graph.request('/2753661784664815/comments?fields=from,message_tags&limit=2500')['data']
# Airpods Giveaway
# data = graph.request('/2753090481388612/comments?fields=from,message_tags&limit=2000')['data']
# data = exampeData

people = {}

for i in range(len(data)):
    name = data[i]['from']['name']
    if 'message_tags' not in data[i]:
        None
    elif data[i]['message_tags'][0]['type'] == 'page':
        None
    else:
        tag = data[i]['message_tags'][0]['name']

        print(name)
        time.sleep(0.0015)

        if name in people.keys():
            if tag not in people[name]:
                people[name].append(tag)
        else:
            newList = []
            newList.append(tag)
            people[name] = newList

listOfNameEntries = []

for person in people.keys():
    for i in range(0, len(people[person])):
        listOfNameEntries.append(person)

def stall():
    print("Gathering Valid Entries....")

stall()

f = open("going.txt", "r", encoding="utf8")
text = f.read()
fbGoingList = text.splitlines()


f = open("attendees.txt", "r", encoding="utf8")
text = f.read()
attendeeList = text.splitlines()

allEntries = fbGoingList+listOfNameEntries+attendeeList+attendeeList+attendeeList

length = len(allEntries)

print("Total valid comments:", len(listOfNameEntries))
time.sleep(0.5)
print("Total Going on Facebook:", len(fbGoingList))
time.sleep(0.5)
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
        time.sleep(1)

    print("Person in position", x)
    ascii_banner = pyfiglet.figlet_format(allEntries[x])
    print(ascii_banner)
    confirm_choice()

picker()