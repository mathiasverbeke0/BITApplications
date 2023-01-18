#!/usr/bin/python3

##################################################################################################################################
# Author: Mathias Verbeke
# Date of creation: 2022/01/16
# Summary: This script reads genes and organisms from an input file and writes the corresponding refseq proteins to an output file
##################################################################################################################################

###################
# Importing modules
###################

import argparse, csv, sys
from eutils import Client

########################
# Command line arguments
########################

parser = argparse.ArgumentParser()

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--api', metavar = '', type = str, required = True, help = 'NCBI API key')
parser.add_argument('-i', '--input', metavar = '', type = str, required = True, help = 'input CSV file')
parser.add_argument('-o', '--output', metavar = '', type = str, required = True, help = 'output file')
parser.add_argument('-d', '--delimiter', metavar = '', required = False, choices = ['comma', 'colon', 'semicolon'], help = 'specify the delimiter used in the input file (default: comma; options: [comma, colon, semicolon])')
parser.add_argument('-H', '--header', action = 'store_true', help = 'use this option if the input file has a header on line 1')

args = parser.parse_args()

###########
# Delimiter
###########

if args.delimiter == 'comma' or args.delimiter == None:
    args.delimiter = ','

elif args.delimiter == 'colon':
    args.delimiter = ':'

elif args.delimiter ==  'semicolon':
    args.delimiter = ';'

#######
# Title
#######

print("\n██████╗ ██████╗  ██████╗ ████████╗    ██████╗ ███████╗███████╗███████╗███████╗ ██████╗     ██████╗ ███████╗████████╗██████╗ ██╗███████╗██╗   ██╗███████╗██████╗ \n\
██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔═══██╗    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝██║   ██║██╔════╝██╔══██╗\n\
██████╔╝██████╔╝██║   ██║   ██║       ██████╔╝█████╗  █████╗  ███████╗█████╗  ██║   ██║    ██████╔╝█████╗     ██║   ██████╔╝██║█████╗  ██║   ██║█████╗  ██████╔╝\n\
██╔═══╝ ██╔══██╗██║   ██║   ██║       ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══╝  ██║▄▄ ██║    ██╔══██╗██╔══╝     ██║   ██╔══██╗██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗\n\
██║     ██║  ██║╚██████╔╝   ██║       ██║  ██║███████╗██║     ███████║███████╗╚██████╔╝    ██║  ██║███████╗   ██║   ██║  ██║██║███████╗ ╚████╔╝ ███████╗██║  ██║\n\
╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝       ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚══════╝ ╚══▀▀═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝\n")

######################################################
# Initialize client that handles all caching and query
######################################################

eclient = Client(api_key = args.api)

##################
# Reading the file
##################

file = open(args.input, "r")
csv_reader = csv.reader(file, delimiter = args.delimiter)
fasta  = open(args.output, "w")

flag = "header_unprocessed"
counter = 0
for line in csv_reader:
    
    if len(line) != 2:

            if len(line) == 1:
                fasta.close()
                sys.exit("Error: The input file contains a mistake on line {}. The delimitor might not be present in this row. Fix this.".format(counter + 1))
            
            elif len(line) > 2:
                fasta.close()
                sys.exit("Error: The input file contains a mistake on line {}. The delimitor might appear several times in this row. Fix this.".format(counter + 1))
            
            elif len(line) == 0:
                counter += 1 
                continue

    if flag == "header_unprocessed" and args.header == True:
        flag = "header_processed"
        print("The columns are:\n----------------\n{} | {}\n".format(line[0], line[1]))

    else:
        gene, organism = line[0].strip(), line[1].strip()
        
        # Fool proofing the input for the esearch
        gene = gene.strip()
        organism_list = organism.split()
        organism = " ".join(organism_list)

        protein_esearch = eclient.esearch(db='protein', term='"{}"[gene] AND "{}" [orgn] AND refseq [filter]'.format(gene, organism))
        print("refseq matches for {} in {}: {}".format(gene, organism, protein_esearch.retmax))
        
        if protein_esearch.retmax == 0:
            print("")
            continue

        for id in range(protein_esearch.retstart, protein_esearch.retmax):
            print("[{} of {}] fetching refseq {} in {}".format(id + 1, protein_esearch.retmax, gene, organism))
            
            protein_efetch = eclient.efetch(db="protein", id = protein_esearch.ids[id])
            genus_species = organism.split()
            
            fasta_header_components = [">{}".format(gene), genus_species[0], genus_species[1], "id={}".format(protein_esearch.ids[id])]
            fasta_header = "_".join(fasta_header_components)

            fasta.write("{}\n".format(fasta_header))
            fasta.write("{}\n".format(protein_efetch.gbseqs[0].sequence))
        
        print("")
    
    counter += 1

file.close()
fasta.close()