#!/usr/bin/python3

#########################################################################################
# Authors: Mathias Verbeke, Guillaume Le Berre
# Date of creation: 2022/12/14
# Usage: This script checks whether a multifasta file has duplicate accession lines
# Input: A multifasta file
# Output: A multifasta file with unique accession lines and their corresponding sequences
# Command line argument 1: The multifasta input file
# Command line argument 2: The output file
#########################################################################################

import sys, os

# check if the correct arguments were provided on the command line
if len(sys.argv) != 3:
    sys.exit("\nError. You need to provide:\n\t- the name or path of the multifasta file on the command line!\n\t- the name or path of the output file (in case that there are duplicate accession numbers)\n")

if not os.path.exists(sys.argv[1]):
    sys.exit("\nError. {} can't be found on your system. Make sure you:\n\t- provide the correct name of the multifasta file.\n\t- provide the correct path (if necessary) to the multifasta file.\n".format(sys.argv[1]))

# open your multifasta input file
file = open(sys.argv[1])

# make a list which will contain all the UNIQUE accession lines
accession_list = []

# make a list which will contain all of the UNIQUE accession lines and corresponding sequences
unique_fasta = []

# create 2 flags
# flag will include/exclude unique/duplicate accession lines and corresponding sequences
# duplicate_flag will report in the end if there were duplicates or not 
flag = "OK"
duplicate_flag = "No"

# make a counter for all of the fasta sequences in the multifasta file
sum = 0


# iterate over every line in the input multifasta file
for line in file.readlines():

    # checks for every accession line
    if line[0] == ">":
        line.strip()
        sum += 1

        # if the accession line is unique (not yet in the list) it will be added to the list
        if line not in accession_list:
            unique_fasta.append(line)
            accession_list.append(line)
            flag = "OK"
        
        # if the accession line is not unique (already in the list) it will be exluded from the list. 
        # the flag becomes NOK, meaning the sequences belonging to the accesion line will not be processed (stored in the unique_fasta list)
        else:
            flag = "NOK"
            duplicate_flag = "Yes"
            continue
    

    elif flag == "OK":
        line.strip()
        unique_fasta.append(line)

    # the sequences belonging to duplicate accession lines will not be processed (stored in the unique_fasta list)    
    elif flag == "NOK":
        continue

file.close()


# If there are duplicates, you create a new file and print all of the unique fasta files.
if duplicate_flag == "Yes":
    output = open(sys.argv[2], "w")

    for x in unique_fasta:
        output.write("{}".format(x))
    
    output.close()
    print("There were in fact duplicates! You can find your multifasta without duplicates at {}.".format(sys.argv[2]))

# If there are no duplicates, you don't even have to open a file to print all of the unique fasta files. 
else:
    print("There were no duplicates! {} only contains fasta sequences with unique accession numbers.".format(sys.argv[1]))