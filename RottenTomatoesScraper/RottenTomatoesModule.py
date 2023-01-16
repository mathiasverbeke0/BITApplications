#!/usr/bin/python3

###############################################################
# Author: Mathias Verbeke
# Date of creation: 2022/01/15
# Summary: This script is a module for RottenTomatoesScraper.py
###############################################################

##################
# Imported modules
##################

import re
from bs4 import BeautifulSoup

#######################################
# Function used during URL construction
#######################################

def UrlConstructer(category, query):
    
    base_url = "https://www.rottentomatoes.com/{}/".format(category)

    url_query = ""

    for i in query:
        
        i = i.lower()

        if i in 'abcdefghijklmnopqrstuvwxyz0123456789':
            url_query = url_query + i

        elif i == ' ':
            url_query = url_query + '_'

        else:
            url_query = url_query + "_"
    
    url_query = url_query.rstrip("_")
    url_query = url_query.lstrip("_")
    url_query = re.sub("_{2, 100}", "_", url_query) 

    url = "{}{}".format(base_url, url_query)

    return url


#############################
# Movies: general information
#############################
def GeneralInformation(soup):
    information = []

    Movie_Info_Section_HTML = soup.find_all("section", {"data-qa": "movie-info-section"})
    Movie_Info_Section_HTML = Movie_Info_Section_HTML[0]

    Synopsis_HTML = Movie_Info_Section_HTML.find_all("div", {"data-qa": "movie-info-synopsis", "id": "movieSynopsis"})
    Synopsis_HTML = Synopsis_HTML[0]
    synopsis = Synopsis_HTML.text
    synopsis = synopsis.strip()
    synopsis_words = synopsis.split()
    synopsis = " ".join(synopsis_words)

    Information_Labels_HTML = Movie_Info_Section_HTML.find_all("div", {"data-qa" : "movie-info-item-label"})
    Information_Values_HTML = Movie_Info_Section_HTML.find_all("div", {"data-qa" : "movie-info-item-value"})

    for i in range(0, len(Information_Labels_HTML)):
        Information_Label_HTML = Information_Labels_HTML[i]
        Information_Value_HTML = Information_Values_HTML[i]

        label = Information_Label_HTML.text
        label = label.strip()
        label_words = label.split()
        label = " ".join(label_words)
        
        value = Information_Value_HTML.text
        value = value.strip()
        value_words = value.split()
        value = " ".join(value_words)
        
        information.append([label, value])
        
    return synopsis, information
    
    
#######################
# Movies: cast and crew
#######################

def CastAndCrew(soup):
    RTCast_Section_HTML = soup.find_all("div", {"class": "castSection", "data-qa": "cast-section"})
    RTCast_Section_HTML = RTCast_Section_HTML[0]

    Cast_Crew_Members_HTML_List = RTCast_Section_HTML.find_all("div", {"data-qa": "cast-crew-item"})
    cast_crew_members_list = []

    for Cast_Crew_Member_HTML in Cast_Crew_Members_HTML_List:
        Member_Role_HTML = Cast_Crew_Member_HTML.find_all("span", {"class": "characters subtle smaller"})
        Member_HTML_Attribute_List = Member_Role_HTML[0].attrs
        member = Member_HTML_Attribute_List["title"]

        Role_Raw = Member_Role_HTML[0].text
        Role_Raw = Role_Raw.strip()
        Role_Raw_Chars = []

        for char in Role_Raw:
            Role_Raw_Chars.append(char)

        while True:
            if '\n' in Role_Raw_Chars:
                Role_Raw_Chars.remove('\n')

            else: break

        Role_Raw = ''.join(Role_Raw_Chars)
        Role_Raw_Chars = Role_Raw.split()
        
        role = ""
        counter = 0

        for word in Role_Raw_Chars:
            if counter == 0:
                role = word

            else:
                role = "{} {}".format(role, word)
            
            counter += 1

        cast_crew_members_list.append([member, role])
    
    return cast_crew_members_list

        



