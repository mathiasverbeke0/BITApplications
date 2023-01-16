#!/usr/bin/python3

########################################################################################################
# Author: Mathias Verbeke
# Date of creation: 2022/01/09
# Summary: This script gives you information about a movie, actor or tv series listed on Rotten Tomatoes
########################################################################################################

##################
# Imported modules
##################

import argparse, urllib, sys
import RottenTomatoesModule as rtmodule
import urllib.request
from bs4 import BeautifulSoup

########################
# Command line arguments
########################

parser = argparse.ArgumentParser()
parser.add_argument('-m', metavar = '"movie"', type = str, required = False, help = 'provide the movie name between parenthesis')
parser.add_argument('-c', action = 'store_true', required = False, help = 'cast & crew')
parser.add_argument('-i', action = 'store_true', required = False, help = 'general information')
parser.add_argument('-u', metavar = 'url', type = str, required = False, help = 'provide the url for a Rotten Tomatoes movie page')
parser.add_argument('-a', metavar = '"actor"', type = str, required = False, help = 'provide the actor name between parenthesis')
parser.add_argument('-H', action = 'store_true', help = 'hide the title and other redundant information')
args = parser.parse_args()

##############################
# Command line arguments check
##############################

argument_list = [args.m, args.u, args.a]
counter = []

for argument in argument_list:
    if argument != None:
        counter.append(argument)
    
    else:
        continue

if args.m == None and args.u == None and args.a == None:
    sys.exit(parser.print_help())
        
if len(counter) > 1:
    sys.exit("RottenTomatoesScraper.py: error: argument -m, -u and -a: invalid combination of arguments: the -m, -u and -a options can not be used together")

###################
# Application title
###################
if args.H == False: 
    print(" ______     ______     ______   ______   ______     __   __        ______   ______     __    __     ______     ______   ______     ______     ______    \n\
/\  == \   /\  __ \   /\__  _\ /\__  _\ /\  ___\   /\ '-.\ \      /\__  _\ /\  __ \   /\ '-./  \   /\  __ \   /\__  _\ /\  __ \   /\  ___\   /\  ___\   \n\
\ \  __<   \ \ \/\ \  \/_/\ \/ \/_/\ \/ \ \  __\   \ \ \-.  \     \/_/\ \/ \ \ \/\ \  \ \ \-./\ \  \ \  __ \  \/_/\ \/ \ \ \/\ \  \ \  __\   \ \___  \  \n\
 \ \_\ \_\  \ \_____\    \ \_\    \ \_\  \ \_____\  \ \_\\'\_\       .\ \_\  \ \_____\  \ \_\ \ \_\  \ \_\ \_\    \ \_\  \ \_____\  \ \_____\  \/\_____\ \n\
  \/_/ /_/   \/_____/     \/_/     \/_/   \/_____/   \/_/ \/_/        \/_/   \/_____/   \/_/  \/_/   \/_/\/_/     \/_/   \/_____/   \/_____/   \/_____/ \n ")

##################
# URL construction
##################

if args.m != None:
    category = "m"
    url = rtmodule.UrlConstructer(category, args.m)

elif args.u != None:
    category = "m"
    url = args.u

elif args.a != None:
    category = "celebrity"
    url = rtmodule.UrlConstructer(category, args.a)

if args.H == False: 
    print("The link '{}' will be used to search for the data.\n".format(url))

##########################################
# Fetching information from rottentomatoes
##########################################

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"

try:
    if args.H == False: 
        print("Connecting to Rotten Tomatoes ...\n")
    
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

except Exception as e:
    sys.exit("{}. Possible reasons include:\n\t- a typo\n\t- unusual symbols in the movie title\n\t- the movie not being listed on Rotten Tomatoes\n\t- Rotten Tomatoes not following its own link construction standards".format(e))

soup = BeautifulSoup(data, 'html.parser')

# writing the prettified soup data to a file (good overview)
# file = open(path, "w")
# file.write(soup.prettify())
# file.close

########################################
# Finding information on Rotten Tomatoes
########################################

if (args.m != None or args.u != None) and args.c == True:
    cast_crew_members_list = rtmodule.CastAndCrew(soup)

if (args.m != None or args.u != None) and args.i == True:
    synopsis, information = rtmodule.GeneralInformation(soup)

if args.a != None:
    print("This option is under construction")

########
# Output
########

if (args.m != None or args.u != None) and args.i == True:
    print("Synopsis:\n---------\n{}".format(synopsis))
    print("\nGeneral information:\n--------------------")

    for item in information:
        print("{} {}".format(item[0], item[1]))

    if args.c == True:
        print("")

if (args.m != None or args.u != None) and args.c == True:
    cast = "unmentioned"
    crew = "unmentioned"
    current_group = "cast"

    for member, role in cast_crew_members_list:
        if role == "": 
            role = "not specified"
        
        if role == "Director":
            current_group = "crew"

        if current_group == "cast":
            if cast == "unmentioned":
                print("Cast:\n-----")
                cast = "mentioned"
            
            print("- {} as {}".format(member, role))
        
        elif current_group == "crew":
            if crew == "unmentioned":
                print("\nCrew:\n-----")
                crew = "mentioned"
            
            print("- {}: {}".format(role, member))