#!/usr/bin/python3

##########################################################################################
# Author: Mathias Verbeke
# Date of creation: 2022/01/09
# Summary: This script gives you the cast and crew of a movie as listed on rotten tomatoes
##########################################################################################

##################
# Imported modules
##################

import argparse, re, urllib
import sys
import urllib.request
from bs4 import BeautifulSoup

########################
# Command line arguments
########################

parser = argparse.ArgumentParser()
parser.add_argument('-m', metavar = '"movie"', type = str, required = True, help = 'provide the movie name between parenthesis')

args = parser.parse_args()

movie = args.m

###################
# Application title
###################

print(" ______     ______     ______   ______   ______     __   __        ______   ______     __    __     ______     ______   ______     ______     ______    \n\
/\  == \   /\  __ \   /\__  _\ /\__  _\ /\  ___\   /\ '-.\ \      /\__  _\ /\  __ \   /\ '-./  \   /\  __ \   /\__  _\ /\  __ \   /\  ___\   /\  ___\   \n\
\ \  __<   \ \ \/\ \  \/_/\ \/ \/_/\ \/ \ \  __\   \ \ \-.  \     \/_/\ \/ \ \ \/\ \  \ \ \-./\ \  \ \  __ \  \/_/\ \/ \ \ \/\ \  \ \  __\   \ \___  \  \n\
 \ \_\ \_\  \ \_____\    \ \_\    \ \_\  \ \_____\  \ \_\\'\_\       .\ \_\  \ \_____\  \ \_\ \ \_\  \ \_\ \_\    \ \_\  \ \_____\  \ \_____\  \/\_____\ \n\
  \/_/ /_/   \/_____/     \/_/     \/_/   \/_____/   \/_/ \/_/        \/_/   \/_____/   \/_/  \/_/   \/_/\/_/     \/_/   \/_____/   \/_____/   \/_____/ \n ")

##################
# URL construction
##################

base_URL = "https://www.rottentomatoes.com/m/"

movie = movie.lower()
movie_simplified = ""

for i in movie:
    
    if i in 'abcdefghijklmnopqrstuvwxyz' or i == " ":
        movie_simplified = "{}{}".format(movie_simplified, i)

    else:
        
        movie_simplified = "{}{}".format(movie_simplified, " ")

movie_simplified = movie_simplified.replace(" ", "_")
movie_simplified = movie_simplified.rstrip("_")
movie_simplified = re.sub("_{2,100}","_", movie_simplified)

url = base_URL + movie_simplified
print("The link '{}' will be used to search for the data.\n".format(url))

##########################################
# Fetching information from rottentomatoes
##########################################

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"

try:
    print("Connecting to Rotten Tomatoes ...\n")
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

except Exception as e:
    sys.exit("The following error occurred: {}\nPossible reasons include a typo, unusual symbols in the movie title, or the movie not being listed on Rotten Tomatoes. Exiting the application.".format(e))

##################
# Making some soup
##################

soup = BeautifulSoup(data, 'html.parser')

# writing the prettified soup data to a file (good overview)
# file = open(path, "w")
# file.write(soup.prettify())
# file.close

###########################
# finding the cast and crew
###########################
cast_section = soup.find_all("div", {"class": "castSection", "data-qa": "cast-section"})
cast_crew_members = cast_section[0].find_all("div", {"data-qa": "cast-crew-item"})
cast_crew_list = []

for cast_crew_member in cast_crew_members:
    member_role = cast_crew_member.find_all("span", {"class": "characters subtle smaller"})
    
    member_attrs = member_role[0].attrs
    member = member_attrs["title"]
    role_raw = member_role[0].text

    role_raw = role_raw.strip()
    listing = []
    
    for item in role_raw:
        listing.append(item)
    
    while True:
        if '\n' in listing:
            listing.remove("\n")
        
        else:
            break

    role_raw = ''.join(listing)
    role_list = role_raw.split()
    role = ""

    counter = 0
    for item in role_list:
        if counter == 0:
            role = item
            
        else:
            role = "{} {}".format(role, item)
        
        counter += 1

    cast_crew_list.append([member, role])

########
# Output
########

flag = "unmentioned"
flag2 = "cast"
flag3 = "unmentioned"
for member, role in cast_crew_list:
    if flag == "unmentioned":
        print("Cast:\n-----")
        flag = "mentioned"
    
    if role == "Director":
        flag2 = "crew"

    if flag2 == "cast":
        if role == "":
            role = "not listed"

        print("- {} as {}".format(member, role))

    elif flag2 == "crew":
        if flag3 == "unmentioned":
            print("\nCrew:\n-----")
            flag3 = "mentioned"
        
        print("- {}: {}".format(role, member))