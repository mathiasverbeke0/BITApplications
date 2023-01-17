#!/usr/bin/python3

#######################################################################################################
# Author: Mathias Verbeke
# Date of creation: 2022/01/17
# Summary: This script scrapes the "bilboard hot 100" page and returns the top selected amount of songs
#######################################################################################################

##################
# Imported modules
##################

import argparse, urllib, sys, csv
import urllib.request
from bs4 import BeautifulSoup

########################
# Command line arguments
########################

parser = argparse.ArgumentParser()

parser.add_argument('-o', metavar = 'output', required = False, type = str, help = 'output file')
parser.add_argument('-n', metavar = 'amount', required = False, type = int, default = 10, help = 'amount of top tunes (default: 10)')

args = parser.parse_args()

##############################
# Command line argument checks
##############################

if args.n > 100:
    sys.exit("TopTunesScraper.py: error: argument -n: invalid argument value: the maximum value for the -n option is 100")

#######
# Title
#######

print("\n███╗   ██╗ ██████╗ ██╗    ██╗    ██████╗ ██╗      █████╗ ██╗   ██╗██╗███╗   ██╗ ██████╗                                \n\
████╗  ██║██╔═══██╗██║    ██║    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██║████╗  ██║██╔════╝ ██╗                            \n\
██╔██╗ ██║██║   ██║██║ █╗ ██║    ██████╔╝██║     ███████║ ╚████╔╝ ██║██╔██╗ ██║██║  ███╗╚═╝                            \n\
██║╚██╗██║██║   ██║██║███╗██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██║██║╚██╗██║██║   ██║██╗                            \n\
██║ ╚████║╚██████╔╝╚███╔███╔╝    ██║     ███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝╚═╝                            \n\
╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝     ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝                                \n\
                                                                                                                       \n\
████████╗ ██████╗ ██████╗      ██████╗██╗  ██╗ █████╗ ██████╗ ████████╗    ████████╗██╗   ██╗███╗   ██╗███████╗███████╗\n\
╚══██╔══╝██╔═══██╗██╔══██╗    ██╔════╝██║  ██║██╔══██╗██╔══██╗╚══██╔══╝    ╚══██╔══╝██║   ██║████╗  ██║██╔════╝██╔════╝\n\
   ██║   ██║   ██║██████╔╝    ██║     ███████║███████║██████╔╝   ██║          ██║   ██║   ██║██╔██╗ ██║█████╗  ███████╗\n\
   ██║   ██║   ██║██╔═══╝     ██║     ██╔══██║██╔══██║██╔══██╗   ██║          ██║   ██║   ██║██║╚██╗██║██╔══╝  ╚════██║\n\
   ██║   ╚██████╔╝██║         ╚██████╗██║  ██║██║  ██║██║  ██║   ██║          ██║   ╚██████╔╝██║ ╚████║███████╗███████║\n\
   ╚═╝    ╚═════╝ ╚═╝          ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝\n")


#########################################
# Fetching information from billboard.com
#########################################

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
url = "https://www.billboard.com/charts/hot-100/"

try:
    print("Fetching the top {} songs of this moment ...\n".format(args.n))
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

except Exception as e:
    sys.exit(e)

soup = BeautifulSoup(data, 'html.parser')

# file = open("music.txt", "w")
# file.write(soup.prettify())
# file.close()

###########################################
# Fetching information from the soup object
###########################################

top_one_HTML = soup.find("a", {"class": "c-title__link lrv-a-unstyle-link", "href": "#"})
top_one = top_one_HTML.text
top_one = top_one.split()
top_one = " ".join(top_one)

top_one_artist_HTML = soup.find("p", {"class": "c-tagline a-font-primary-l a-font-primary-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-tb-00 lrv-u-padding-t-025 lrv-u-margin-r-150"})
top_one_artist = top_one_artist_HTML.text
top_one_artist = top_one_artist.split()
top_one_artist = " ".join(top_one_artist)

songs_HTML = soup.find_all("h3", {"class": "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only", "id": "title-of-a-story"})
artists_HTML = soup.find_all("span", {"class": "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"})

if args.o == None:
    print("The top {} tunes at this moment are: ".format(args.n))
    print("☆ {} | {}".format(top_one, top_one_artist))

else: 
    output = open(args.o, "w")
    output_writer = csv.writer(output, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_MINIMAL)


for i in range(1, args.n):
    song = songs_HTML[i-1].text
    song = song.split()
    song = " ".join(song)

    artist = artists_HTML[i-1].text
    artist = artist.split()
    artist = " ".join(artist)

    if args.o == None: 
        print("☆ {} | {}".format(song, artist))

    else:
        output_writer.writerow([song, artist])

if args.o != None:
    output.close()