#!/usr/bin/env python
__author__ = "Steve Gilissen - http://www.gilissen.me - https://github.com/sgilissen"
__credits__ = ["Steve Gilissen"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Steve Gilissen"

import urllib.request
import json
import sys
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-s", "--street", dest="verbose", help="Find the street name. Specify the NIS code of the municipality to get best results.")
parser.add_argument("-m", "--municipality", dest="verbose", help="Find the municipality.")
parser.add_argument("-c", "--calendar", dest="verbose", help="Show the calendar.")
args = parser.parse_args()
parser.print_help()

baseAPI = "https://api.limburg.net/public/"
# API extensions:
#
# afval-kalender/  -  Used to perform searches
# kalender/ - Used to show the upcoming dates
searchAPIExtension = "afval-kalender/"
calendarAPIExtension = "kalender/"



def findMunicipality(municipality):
    req = urllib.request.Request(baseAPI + searchAPIExtension)
    print("Found the following municipalities:")


def findStreet(street, nisCode):
    req = urllib.request.Request(baseAPI + searchAPIExtension)
    print("Found the following streets:")

def findEvents():
    req = urllib.request.Request(baseAPI + calendarAPIExtension)
    print("Found the following events:")
