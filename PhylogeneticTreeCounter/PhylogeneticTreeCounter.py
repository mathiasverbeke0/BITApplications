#!/usr/bin/python3

##############################################################################################################
# Author: Mathias Verbeke
# Date of creation: 2022/01/02
# Usage: This script calculates the number of OTUs, rooted trees and unrooted trees
# Input: The amount of OTUs, the amount of rooted trees or the amount of unrooted trees
# Output: The amount of OTUs, the amount of rooted trees and the amount of unrooted trees
##############################################################################################################

################
# Import modules 
################                                                                                                                                    

import sys

##################
# Define functions
##################

# Define function that uses the amount of OTUs as input and prints the amount of (un)rooted trees 

def all_trees (OTU):

    if OTU < 2:
        sys.exit("Invalid amount of OTUs.\n")
    
    # Calculate the double factorial (or semifactorial) of the unrooted term (2n-5) and the rooted term (2n-3)

    if OTU > 1000:
        sys.exit("The amount of OTUs is out of range.\n")

    else:
        result = 1
        unrooted_term = (2*OTU)-5
         
        for i in range(unrooted_term, 0, -2):
            result *= i

        print("Amount of unrooted trees: {}".format(result))
    
        result = 1
        rooted_term = (2*OTU)-3
        
        for i in range(rooted_term, 0, -2):
            result *= i
        
        print("Amount of rooted trees: {}".format(result))


# Define function that uses the amount of the amount of unrooted trees as input and prints the amount of OTUs and the amount of rooted trees

def rooted_from_unrooted (unrooted):
    collection = []

    # Check if the provided amount of unrooted trees matches with a specific amount of OTUs (upper limit is 1000 OTUs)
    # If there is a match, print the amount of OTUs and the amount of rooted trees 

    for j in range(2,1001):
        result = 1
        unrooted_term = (2*j)-5
        for i in range(unrooted_term, 0, -2):
            result *= i
        
        if result == unrooted:
            collection.append(result)

            OTUs = j
            result = 1
            rooted_term = (2*OTUs) - 3

            for i in range(rooted_term, 0, -2):
                result *= i

            print("Amount of OTUs: {}".format(OTUs))
            print("Amount of rooted trees: {}".format(result))
            print("")
            
            
            break
        
        else:
            collection.append(result)

    if unrooted not in collection:
        sys.exit("The amount of unrooted trees does not match a specific amount of OTUs or is out of range.\n")


# Define function that uses the amount of the amount of rooted trees as input and prints the amount of OTUs and the amount of unrooted trees

def unrooted_from_rooted (rooted):
    collection = []

    # Check if the provided amount of rooted trees matches with a specific amount of OTUs (upper limit is 1000 OTUs)
    # If there is a match, print the amount of OTUs and the amount of unrooted trees 

    for j in range(2,1001):
        result = 1
        rooted_term = (2*j)-3
        for i in range(rooted_term, 0, -2):
            result *= i
        
        if result == rooted:
            collection.append(result)

            OTUs = j
            result = 1
            unrooted_term = (2*OTUs) - 5

            for i in range(unrooted_term, 0, -2):
                result *= i

            print("Amount of OTUs: {}".format(OTUs))
            print("Amount of unrooted trees: {}".format(result))
            print("")
            
            
            break
        
        else:
            collection.append(result)

    if rooted not in collection:
        sys.exit("The amount of rooted trees does not match a specific amount of OTUs or is out of range.\n") 

###########################
# Define the user interface
###########################

print(" ____  _   ___   ___     ___   ____ _____ _   _ _____ _____ ___ ____   _____ ____  _____ _____    ____ ___  _   _ _   _ _____ _____ ____  \n\
|  _ \| | | \ \ / | |   / _ \ / ___| ____| \ | | ____|_   _|_ _/ ___| |_   _|  _ \| ____| ____|  / ___/ _ \| | | | \ | |_   _| ____|  _ \ \n\
| |_) | |_| |\ V /| |  | | | | |  _|  _| |  \| |  _|   | |  | | |       | | | |_) |  _| |  _|   | |  | | | | | | |  \| | | | |  _| | |_) |\n\
|  __/|  _  | | | | |__| |_| | |_| | |___| |\  | |___  | |  | | |___    | | |  _ <| |___| |___  | |__| |_| | |_| | |\  | | | | |___|  _ < \n\
|_|   |_| |_| |_| |_____\___/ \____|_____|_| \_|_____| |_| |___\____|   |_| |_| \_|_____|_____|  \____\___/ \___/|_| \_| |_| |_____|_| \_\ \n")

while True:
    
    print("[1] number of OTUs [2] number of unrooted trees [3] number of rooted trees [q] quit ")
    
    info = input("What information do you have? ") 
    
    if info in ["1", "2", "3"]:
        info =  int(info)
        break

    elif info == "q":
        sys.exit("")

    else:
        print("Try again.\n")

print("")

if info == 1:

    while True:
        
        OTU = input("Give the amount of OTUS: ")
        
        if OTU == "q":
            sys.exit("")

        try:
            OTU_integer = int(OTU)
        
        except:
            print("Invalid input. Try again or press q to quit. \n")
            continue
    
        print("")
        all_trees(OTU_integer)
        print("")
        break


if info == 2:

    while True:
        
        unrooted = input("Give the amount of unrooted trees: ")
        
        if unrooted == "q":
            sys.exit("")

        try:
            unrooted_integer = int(unrooted)
        
        except:
            print("Invalid input. Try again or press q to quit. \n")
            continue
    
        print("")
        rooted_from_unrooted(unrooted_integer)
        print("")
        break

if info == 3:

    while True:
        
        rooted = input("Give the amount of rooted trees: ")
        
        if rooted == "q":
            sys.exit("")

        try:
            rooted_integer = int(rooted)
        
        except:
            print("Invalid input. Try again or press q to quit. \n")
            continue
    
        print("")
        unrooted_from_rooted(rooted_integer)
        print("")
        break