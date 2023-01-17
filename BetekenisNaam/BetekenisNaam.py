#!/usr/bin/python3

################################################################################
# Author: Mathias Verbeke
# Date of creation: 2022/01/17
# Summary: Dit python script geeft de betekenis van je naam als je deze invoert.
################################################################################

##################
# Imported modules
##################

import argparse, urllib, sys
import urllib.request
from bs4 import BeautifulSoup

########################
# Command line arguments
########################

parser = argparse.ArgumentParser()

parser.add_argument('-n', metavar = 'naam', required = True, type = str, help = 'naam waarvan je de betekenis wil opzoeken')

args = parser.parse_args()

##############################
# Command line argument checks
##############################

args.n = (args.n).strip()
args.n = (args.n).lower()

for char in args.n:
    if char not in 'abcdefghijklmnopqrstuvwxyz':
        sys.exit("BetekenisNaam.py: error: argument -n: De website waarvan de informatie wordt gehaald, kan helaas niet om met het teken '{}'.".format(char))

#######
# Title
#######

print("\n██████╗ ███████╗████████╗███████╗██╗  ██╗███████╗███╗   ██╗██╗███████╗    ███╗   ██╗ █████╗  █████╗ ███╗   ███╗\n\
██╔══██╗██╔════╝╚══██╔══╝██╔════╝██║ ██╔╝██╔════╝████╗  ██║██║██╔════╝    ████╗  ██║██╔══██╗██╔══██╗████╗ ████║\n\
██████╔╝█████╗     ██║   █████╗  █████╔╝ █████╗  ██╔██╗ ██║██║███████╗    ██╔██╗ ██║███████║███████║██╔████╔██║\n\
██╔══██╗██╔══╝     ██║   ██╔══╝  ██╔═██╗ ██╔══╝  ██║╚██╗██║██║╚════██║    ██║╚██╗██║██╔══██║██╔══██║██║╚██╔╝██║\n\
██████╔╝███████╗   ██║   ███████╗██║  ██╗███████╗██║ ╚████║██║███████║    ██║ ╚████║██║  ██║██║  ██║██║ ╚═╝ ██║\n\
╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝╚══════╝    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝\n")

#############################################
# Fetching information from betekenisnamen.nl
#############################################

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
url = "https://www.betekenisnamen.nl/naam/{}".format(args.n)

try:
    print("De betekenis van {} wordt gezocht ...\n".format((args.n).capitalize()))
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

except Exception as e:
    sys.exit(e)

soup = BeautifulSoup(data, 'html.parser')

file = open("naam.txt", "w")
file.write(soup.prettify())
file.close()

###########################################
# Fetching information from the soup object
###########################################

meaning_HTML = soup.find("div", {"class": "container body-content my-2"})
meaning_HTML = meaning_HTML.find_all("p")
meaning = meaning_HTML[2].text
meaning = meaning.split(";")
meaning = ", ".join(meaning)

if meaning.capitalize() == "Staat jouw naam er niet bij? dat kan natuurlijk niet, voer deze hier in en wij gaan deze zo snel mogelijk toevoegen!" or meaning.strip() == "":
    sys.exit("Betekenis niet gevonden.\n")

print("Betekenis: {}\n".format(meaning.capitalize()))