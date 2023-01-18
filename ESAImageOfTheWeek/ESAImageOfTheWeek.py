#!/usr/bin/python3

###########################################################################################
# Author: Mathias Verbeke
# Date of creation: 2022/01/18
# Summary: allows you to search download the "Earth observation of the week" image from ESA
###########################################################################################

##################
# Imported modules
##################

import argparse, urllib, sys, wget, re
import urllib.request
from bs4 import BeautifulSoup

########################
# Command line arguments
########################

parser = argparse.ArgumentParser()
parser.add_argument('-d', metavar = 'directory', type = str, required = False, help = 'directory where you want to store the picture')

args = parser.parse_args()

#######
# Title
#######

print("\n███████╗ █████╗ ██████╗ ████████╗██╗  ██╗     ██████╗ ██████╗ ███████╗███████╗██████╗ ██╗   ██╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗    \n\
██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║  ██║    ██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██║   ██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║    \n\
█████╗  ███████║██████╔╝   ██║   ███████║    ██║   ██║██████╔╝███████╗█████╗  ██████╔╝██║   ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║    \n\
██╔══╝  ██╔══██║██╔══██╗   ██║   ██╔══██║    ██║   ██║██╔══██╗╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══██║   ██║   ██║██║   ██║██║╚██╗██║    \n\
███████╗██║  ██║██║  ██║   ██║   ██║  ██║    ╚██████╔╝██████╔╝███████║███████╗██║  ██║ ╚████╔╝ ██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║    \n\
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    \n\
                                                                                                                                          \n\
██╗███╗   ███╗ █████╗  ██████╗ ███████╗     ██████╗ ███████╗    ████████╗██╗  ██╗███████╗    ██╗    ██╗███████╗███████╗██╗  ██╗           \n\
██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝    ██╔═══██╗██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ██║    ██║██╔════╝██╔════╝██║ ██╔╝           \n\
██║██╔████╔██║███████║██║  ███╗█████╗      ██║   ██║█████╗         ██║   ███████║█████╗      ██║ █╗ ██║█████╗  █████╗  █████╔╝            \n\
██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝      ██║   ██║██╔══╝         ██║   ██╔══██║██╔══╝      ██║███╗██║██╔══╝  ██╔══╝  ██╔═██╗            \n\
██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗    ╚██████╔╝██║            ██║   ██║  ██║███████╗    ╚███╔███╔╝███████╗███████╗██║  ██╗           \n\
╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝            ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝           \n")

###########
# Variables
###########

if args.d == None:
    args.d = "."

elif re.match("/", args.d) != None:
    args.d = args.d

else:
    args.d = (args.d).split("/")
    args.d = "/".join(args.d)
    args.d = "{}".format(args.d)

###############################
# Fetching information from ESA
###############################

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
url = "https://www.esa.int/ESA_Multimedia/Sets/Earth_observation_image_of_the_week/(result_type)/images"

try:
    print("Fetching information from ESA ...\n")
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

except Exception as e:
    sys.exit("{}\nYou are unable to fetch information from ESA!\n".format(e))

soup = BeautifulSoup(data, 'html.parser')

file = open("/home/guest/PythonScripting/Applications/ESAImageScraper/raw.txt", "w")
file.write(soup.prettify())
file.close()

#############################################
# Extracting information from the soup object
#############################################

image_HMTL = soup.find("img", {"class": "image-bg"})
image_attrs = image_HMTL.attrs
image_location = image_attrs['src']
image_link = "https://www.esa.int/{}".format(image_location)
image_alt_raw = image_attrs['alt']
image_alt = ""

for char in image_alt_raw:
    if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
        image_alt = "{}{}".format(image_alt, char)
    
    else:
        continue 

image_alt = "{}.png".format(image_alt)

wget.download(image_link, out = "{}/{}".format(args.d, image_alt))

if args.d == ".":
    print("\n\n{} has been saved in the current directory.".format(image_alt))

else:
    print("\n\n{} has been saved in {}.".format(image_alt, args.d))