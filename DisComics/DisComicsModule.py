##################
# Imported modules
##################

import argparse, urllib, sys
import urllib.request
from bs4 import BeautifulSoup

###################################################
# Function to get information from the soup objects
###################################################

def SoupParser(soup, comic_type, character, count, pages):

    if count == 0:
        message = "Page 1"
        print("\n{}\n{}\n{}\n".format("-" * len(message), message, "-" * len(message)))

    elif count != 0:
        message = "Page {}".format(count + 1)
        print("\n{}\n{}\n{}\n".format("-" * len(message), message, "-" * len(message)))

        url = "https://www.bol.com/be/nl/s/?page={}&searchtext={}comics{}&view=list&filter_N=8292+11209+14033+58334&N=8299&rating=all".format(count + 1, comic_type, character)

        ###################################
        # Fetching information from bol.com
        ###################################
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"

        try:
            request = urllib.request.Request(url, headers = headers)
            response = urllib.request.urlopen(request)
            data = response.read().decode("utf-8")

        except Exception as e:
            sys.exit("{}\nYou are unable to fetch information from bol.com!\n".format(e))

        soup = BeautifulSoup(data, 'html.parser')

    title_subtitle_HTML = soup.find_all("div", {"class": "product-item__info hit-area"})
    price_HTML = soup.find_all("span", {"class": "promo-price", "data-test": "price"})
    niet_leverbaar = soup.find("span", {"class": "product-prices__bol-price"})
    
    if niet_leverbaar != None and pages == 1:
        print("No matches.\n")

    elif niet_leverbaar != None:
        print("This page contains prices that say 'niet leverbaar'. In this stage of development, these cause an error.\nThe application will skip to the next page.\n")

    else:
        specs_HTML = soup.find_all("ul", {"class": "product-small-specs"})

        for i in range(0, len(title_subtitle_HTML)):
            title_HTML = title_subtitle_HTML[i].find("a", {"data-list-page-product-click-location": "title"})
            title = title_HTML.text
            title_components = title.split()
            title = " ".join(title_components)
            print("{}:".format(title))
            print("-" * (len(title) + 1))

            subtitle_HTML = title_subtitle_HTML[i].find("div", {"class": "product-subtitle", "data-test": "product-sub-title"})
            
            if subtitle_HTML != None:
                subtitle = subtitle_HTML.text
                subtitle_components = subtitle.split()
                subtitle = " ".join(subtitle_components)
                print("   ■ Subt: {}".format(subtitle))

            price = price_HTML[i].text
            price = price.split()
            price = ".".join(price)
            price = "€ {}".format(price)
            print("   ■ Cost: {}".format(price))

            info_HTML = specs_HTML[i].find_all("span")

            counter = 0
            for u in info_HTML:
                info = u.text

                if counter == 0:
                    print("   ■ Lang: {}".format(info))
                
                elif counter == 1:
                    print("   ■ Form: {}".format(info))

                elif counter == 4:
                    print("   ■ Page: {}".format(info.strip("pagina's")))
                
                counter += 1
            
            print("")