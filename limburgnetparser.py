#!/usr/bin/env python
__author__ = "Steve Gilissen - http://www.gilissen.me - https://github.com/sgilissen"
__credits__ = ["Steve Gilissen"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Steve Gilissen"

import urllib.request
import json
import pprint
import sys
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-s", "--street", dest="street", action='store', help="Find the street name. Usage: STREET NIS")
parser.add_argument("-m", "--municipality", dest="municipality", action='store', help="Find the municipality.")
parser.add_argument("-c", "--calendar", dest="calendar", help="Show the calendar for ID.")
args = parser.parse_args()
#parser.print_help()




baseAPI = "https://api.limburg.net/public/"
# API extensions:
#
# afval-kalender/  -  Used to perform searches
# kalender/ - Used to show the upcoming dates
searchAPIExtension = "afval-kalender/"
calendarAPIExtension = "kalender/"



def findMunicipality(municipality):
    req = urllib.request.Request(baseAPI + searchAPIExtension + "gemeenten/search?query=" + municipality)
    print("Found the following municipalities for " + municipality + ":")
    response = urllib.request.urlopen(req)
    data = response.read()
    #print(data.decode('utf-8'))
    parsed_data = json.loads(data)
    pprint.pprint(parsed_data)



def findStreet(street, nisCode):
    req = urllib.request.Request(baseAPI + searchAPIExtension)
    print("Found the following streets:")
    print(street)

def findEvents():
    req = urllib.request.Request(baseAPI + calendarAPIExtension)
    print("Found the following events:")


if (args.street):
    findStreet()
elif (args.municipality):
    #print(args.municipality)
    findMunicipality(args.municipality)
elif (args.calendar):
    print("calendar")
else:
    parser.print_help()
