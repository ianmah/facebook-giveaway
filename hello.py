import requests
import json
import facebook
import configparser
from random import randint
import time

print('Gathering all entries...')

config = configparser.ConfigParser()
config.read('config.ini')

token = config['DEFAULT']['TOKEN']

graph = facebook.GraphAPI(access_token=token, version = 3.3)

exampeData = [
    {
      "from": {
        "name": "Ben Hwang",
        "id": "2367784543291937"
      },
      "message_tags": [
        {
          "id": "1969632043120882",
          "length": 12,
          "name": "Rebecca Chen",
          "offset": 0,
          "type": "user"
        }
      ],
      "id": "2126961517334848_2127166563981010"
    },
    {
      "from": {
        "name": "Joshua Ansari",
        "id": "2001222153248991"
      },
      "message_tags": [
        {
          "id": "2001558346596966",
          "length": 9,
          "name": "Sam Dover",
          "offset": 0,
          "type": "user"
        }
      ],
      "id": "2126961517334848_2139726566058343"
    },
    {
      "from": {
        "name": "David Tran",
        "id": "1903757956386105"
      },
      "message_tags": [
        {
          "id": "2404926489549046",
          "length": 11,
          "name": "Reza Rezaei",
          "offset": 0,
          "type": "user"
        }
      ],
      "id": "2126961517334848_2129430653754601"
    },
    {
      "from": {
        "name": "David Tran",
        "id": "1790085794436533"
      },
      "message_tags": [
        {
          "id": "1439969312773476",
          "length": 5,
          "name": "Kaiz Bhatia",
          "offset": 0,
          "type": "user"
        }
      ],
      "id": "2126961517334848_2128006493897017"
    },
    {
      "from": {
        "name": "David Tran",
        "id": "1790085794436533"
      },
      "message_tags": [
        {
          "id": "2522622981089083",
          "length": 11,
          "name": "Kaiz Bhatia",
          "offset": 0,
          "type": "user"
        }
      ],
      "id": "2126961517334848_2128010507229949"
    }
  ]
# Smart TV Giveaway
data = graph.request('/2753661784664815/comments?fields=from,message_tags&limit=2500')['data']
# Airpods Giveaway
# data = graph.request('/2753090481388612/comments?fields=from,message_tags&limit=2500')['data']
# data = exampeData

my_list = []


class Person:

    __tags = []
    __name = ''

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_tags(self):
        return self.__tags

    def add_tag(self, tag):
        self.__tags.append(tag)

for i in range(len(data)):

    name = data[i]['from']['name']
    if 'message_tags' not in data[i]:
        None
        # print(name, ' didnt tag anyone')
    elif data[i]['message_tags'][0]['type'] == 'page':
        None
    else:

        tag = data[i]['message_tags'][0]['name']

        n = Person(name)

        currentUsers = []

        for p in my_list:
            currentUsers.append(p.get_name())
        if name not in currentUsers:
            my_list.append(n)
            print(n.get_name())
        else:
            for p in my_list:
                if p.get_name() == name:
                    if tag not in p.get_tags():
                            n.add_tag(tag)
                            my_list.append(n)
                            print(n.get_name())


unchecked = []
for i in range(len(data)):
    name = data[i]['from']['name']
    unchecked.append(name)

currentUsers = []

for p in my_list:
    currentUsers.append(p.get_name())

print('Total entries:', len(my_list))
time.sleep(1)

x = randint(0, len(my_list)-1)
print('Winner number:', x)
time.sleep(1)

print('Person in number', x, 'is')
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print(my_list[x].get_name(), '!')
time.sleep(1)
print('ʕノ•ᴥ•ʔノ CONGRATS!!! ~(˘▾˘~)')
