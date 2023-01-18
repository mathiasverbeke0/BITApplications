#!/usr/bin/python3

##################
# Imported modules
##################

import argparse, urllib, sys, DisComicsModule
import urllib.request
from bs4 import BeautifulSoup

########################
# Command line arguments
########################

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--DC', action = 'store_true', required = False, help = 'DC comics')
parser.add_argument('-m', '--marvel', action = 'store_true', required = False, help = 'marvel comics')
parser.add_argument('-c', '--char', required = False, type = str, help = 'specific character')
parser.add_argument('-a', '--all', action = 'store_true', required = False, help = 'all comics')
parser.add_argument('-s', '--show', action = 'store_true', required = False, help = 'show all pages')

args = parser.parse_args()

##############################
# Command line argument checks
##############################

if args.all == False and args.DC == False and args.marvel == False:
    sys.exit("Discomics.py: error: lack of arguments: You have to use one of these options: -all, -DC or -marvel")

if (args.DC != False or args.marvel != False) and args.all != False:
    sys.exit("Discomics.py: error: argument -all: Do you want all comics or do you want comics from DC/marvel? Make up your mind.")

if args.DC != False and args.marvel != False:
    sys.exit("Discomics.py: error: argument -DC and -marvel: Do you want comics from DC or from marvel? Make up your mind.")

#######
# Title
#######

print("\n██████╗ ██╗███████╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗███████╗\n\
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗████╗ ████║██║██╔════╝██╔════╝\n\
██║  ██║██║███████╗██║     ██║   ██║██╔████╔██║██║██║     ███████╗\n\
██║  ██║██║╚════██║██║     ██║   ██║██║╚██╔╝██║██║██║     ╚════██║\n\
██████╔╝██║███████║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╗███████║\n\
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝╚══════╝\n")

######################
# Constructing the URL
######################

if args.all == True:
    comic_type = ""

elif args.DC == True:
    comic_type = "DC+"

elif args.marvel == True:
    comic_type = "marvel+" 

if args.char != None:
    char_components = (args.char).split()
    args.char = "+".join(char_components)
    character = "+{}".format((args.char)) 

else: 
    character = ""

url = "https://www.bol.com/be/nl/s/?page=1&searchtext={}comics{}&view=list&filter_N=8292+11209+14033+58334&N=8299&rating=all".format(comic_type, character)

###################################
# Fetching information from bol.com
###################################
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"

try:
    print("Fetching information from bol.com ...\n")
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

except Exception as e:
    sys.exit("{}\nYou are unable to fetch information from bol.com!\n".format(e))

soup = BeautifulSoup(data, 'html.parser')

file = open("/home/guest/PythonScripting/Applications/DisComics/raw.txt", "w")
file.write(soup.prettify())
file.close()

##############################
# Checking the amount of pages
##############################

pages_HTML = soup.find("div", {"class": "u-pb--sm", "id": "js_pagination_control"})
other_pages = soup.find_all("a", {"class": "js_pagination_item"})

if len(other_pages) == 0:
    pages = 1
    print("Only 1 page.")

else:
    total_pages = other_pages[len(other_pages) - 1]
    pages = total_pages.text
    pages = pages.strip()
    pages = int(pages)

    print("{} pages.".format(pages))

######################################
# Get information from the soup object
######################################

if args.show == False or pages == 1: 
    DisComicsModule.SoupParser(soup, None, None, 0, pages)

#####################################################
# Get informtaion from the soup object
# Construct new soup objects
# Get information from these new soup objects as well
#####################################################

elif args.show == True and pages > 1:
    for a in range(0, pages):


        if a == 0:
            DisComicsModule.SoupParser(soup, None, None, a, pages)
        
        else: 
            DisComicsModule.SoupParser(soup, comic_type, character, a, pages)

        while True:
            question = input("Type 'n' to go to the next page (or q to exit): ")

            if question == "n":
                break

            elif question == "q":
                sys.exit("")