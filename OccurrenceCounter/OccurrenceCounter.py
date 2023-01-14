#!/usr/bin/python3

#####################################################################################################################
# Author: Mathias Verbeke
# Date of creation: 2022/01/14
# Summary: This script counts the occurrences of items in a specific column of a CSV file and visualizes the results.
#####################################################################################################################

###################
# Importing modules
###################

import csv, argparse, sys
import matplotlib.pyplot as plt
from openpyxl import Workbook

########################
# Command line arguments
########################

parser = argparse.ArgumentParser()

parser = argparse.ArgumentParser(description='Process some CSV data')

parser.add_argument('-i', metavar = 'input.csv', type = str, required = True, help = 'Input CSV file path')
parser.add_argument('-d', metavar = 'delimiter', required = True, choices = ['tab','comma', 'colon', 'semicolon'], help = 'Specify the delimiter used in the input file. Options: [tab, comma, colon, semicolon]')
parser.add_argument('-c', metavar = 'column', type = int, required = True, help = 'Specify the column in the input file where the item is located')
parser.add_argument('-H', action = 'store_true', help = 'The input file contains a header')
parser.add_argument('-l', action = 'store_true', help = 'List items and their occurrence')
parser.add_argument('-e', action = 'store_true', help = 'Write list to excel file')
parser.add_argument('-s', action = 'store_true', help = 'Sort the items descendingly based on their occurrence')
parser.add_argument('-g', action = 'store_true', help = 'Generate an image')
parser.add_argument('-n', metavar = 'items', type = int, default = 10, help = 'Number of items to include in the bar plot (default: 10)')
parser.add_argument('-a', action = 'store_true', help = 'Include all items in the bar plot')
parser.add_argument('-t', metavar = 'title', type = str, default = 'Occurence per item', help = 'Title for the bar plot')
parser.add_argument('-x', metavar = 'name', type = str, default = 'Occurrence', help='Label for the occurences (default: Occurence)')
parser.add_argument('-y', metavar = 'name', type = str, default = 'Item', help='Label for the items (default: Item)')

args = parser.parse_args()

##############################
# Command line argument checks
##############################

if args.e and not args.l:
    sys.exit('OccurenceCounter.py: error: argument -e: invalid combination of arguments: the -e option can only be used with the -l option')

if args.n != 10 and args.a == True:
    sys.exit('OccurenceCounter.py: error: argument -n and -a: invalid combination of arguments: the -n and -e option can not be used together')

if args.n != 10 and args.l == True and args.g == False:
    sys.exit('OccurenceCounter.py: error: argument -n and -l: illogical combination of arguments: the usage of the -n and -l option without the -g option does not make sense (list not connected to a barplot can not be limited with the -n option)')
#####################
# Important variables
#####################

# Filenames
filename = args.i
filename = filename.split(".")
filename = filename[0]
filename_excel = "{}.xlsx".format(filename)
filename_barplot = "{}.png".format(filename)

# Delimiter
if args.d == 'comma':
    args.d = ','

elif args.d == 'tab':
    args.d = '\t'

elif args.d == 'colon':
    args.d = ':'

elif args.d ==  'semicolon':
    args.d = ';'

################################
# Reading and parsing input file
################################

inputFile = open(args.i, "r")
csv_reader = csv.reader(inputFile, delimiter = args.d)

items = {}

for line in csv_reader:
    
    if args.H == True:
        args.H = False
        continue

    if line[args.c] not in items.keys():
        items[line[args.c]] = 0

    items[line[args.c]] += 1 

inputFile.close()

########################################################################
# Command line argument check that was not possible before parsing input
########################################################################

if args.n > len(items):
    args.n = len(items)
    print("\nADJUSTMENT: You wanted the top {} ")

#############################
# Sorting and selecting items
#############################

# Sorting items based on their occurence (only if image is generated or if list needs to be sorted descendingly)
if args.s == True or args.g == True:
    sortedItems = dict(sorted(items.items(), key=lambda item: item[1], reverse = True))

# Determining highest occurring items (only if image is generated)
if args.g == True:
    biggestItems = []
    biggestOccurrences = []

    if args.a == True:
        args.n = len(sortedItems)

    counter = 0
    for item, occurrence in sortedItems.items():
        if counter == args.n:
            break

        biggestItems.append(item)
        biggestOccurrences.append(occurrence)
        counter += 1

if args.g == True and args.l == True:
    
    biggestItemsLibrary = {}
    
    for i in range(0, len(biggestItems)):
        biggestItemsLibrary[biggestItems[i]] = biggestOccurrences[i]

########################################################
# Generating output occurence list not linked to barplot
########################################################

status = "sorted"

if args.l == True and args.g == False:
    
    if args.s == False:
        status = "unsorted"
        sortedItems = items

    # Writing to Excel
    if args.e == True: 
        wb = Workbook()
        ws = wb.active
        ws.title = args.t
        ws.append([args.y, args.x])

        for item, occurence in sortedItems.items():
            ws.append([item, occurence])

        wb.save(filename_excel)
        wb.close()
        print("\n{} xlsx file has been saved at: {}".format(status, filename_excel))
    
    # Writing in the terminal
    else:
        for item, occurence in sortedItems.items():
            print("{}: {}".format(item, occurence))

####################################################
# Generating output occurence list linked to barplot
####################################################

status = "sorted"
if args.l == True and args.g == True:
    
    # Writing to Excel
    if args.e == True: 
        wb = Workbook()
        ws = wb.active
        ws.title = args.t
        ws.append([args.y, args.x])

        for item, occurence in biggestItemsLibrary.items():
            ws.append([item, occurence])

        ws.append("")
        ws.append("\nNOTE: This item list is linked to a barplot")

        wb.save(filename_excel)
        wb.close()
        print("{} xlsx file has been saved at: {}".format(status, filename_excel))
    
    # Writing in the terminal
    else:
        for item, occurence in biggestItemsLibrary.items():
            print("{}: {}".format(item, occurence))

        print("\nNOTE: This item list is linked to a barplot")

# Generating a barplot
if args.g == True:
    plt.barh(biggestItems, biggestOccurrences, color = 'yellowgreen')
    plt.xlabel(args.x)
    plt.ylabel(args.y)
    plt.title(args.t)
    figure = plt.gcf()
    figure.savefig(filename_barplot)

    if args.l == True and args.g == True:
        print("image has been saved at: {}".format(filename_barplot))
    
    else:
        print("\nimage has been saved at: {}".format(filename_barplot))