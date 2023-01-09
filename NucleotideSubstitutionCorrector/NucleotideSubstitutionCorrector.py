#!/usr/bin/python3

#######################################################################################################
# Author: Mathias Verbeke
# Date of creation: 2022/01/09
# Usage: This script corrects the amount of observed nucleotide substitutions using 3 different models.
# Input: The amount of observed nucleotide substitutions
# Output: 3 corrected amounts of nucleotide substitutions
#######################################################################################################

##################
# Imported modules
##################

from numpy import log as ln

#######
# Title
#######

print(" _   _ _   _  ____ _     _____ ___ _____ ___ ____  _____   ____  _   _ ____ ____ _____ ___ _____ _   _ _____ ___ ___  _   _    ____ ___  ____  ____  _____ ____ _____ ___  ____  \n\
| \ | | | | |/ ___| |   | ____/ _ |_   _|_ _|  _ \| ____| / ___|| | | | __ / ___|_   _|_ _|_   _| | | |_   _|_ _/ _ \| \ | |  / ___/ _ \|  _ \|  _ \| ____/ ___|_   _/ _ \|  _ \ \n\
|  \| | | | | |   | |   |  _|| | | || |  | || | | |  _|   \___ \| | | |  _ \___ \ | |  | |  | | | | | | | |  | | | | |  \| | | |  | | | | |_) | |_) |  _|| |     | || | | | |_) |\n\
| |\  | |_| | |___| |___| |__| |_| || |  | || |_| | |___   ___) | |_| | |_) ___) || |  | |  | | | |_| | | |  | | |_| | |\  | | |__| |_| |  _ <|  _ <| |__| |___  | || |_| |  _ < \n\
|_| \_|\___/ \____|_____|_____\___/ |_| |___|____/|_____| |____/ \___/|____|____/ |_| |___| |_|  \___/  |_| |___\___/|_| \_|  \____\___/|_| \_|_| \_|_____\____| |_| \___/|_| \_\ \n")

############
# User input
############

while True:
    nuc = input("Observed amount of nucleotide substitutions: ")
    seq = input("Sequence length: ")
    
    try:
        nuc = float(nuc)
        seq = float(seq)
        
        if nuc > seq:
            print("\nInvalid input!\nTry again.\n")
            continue
        
        print("")
        break

    except:
        print("\nInvalid input!\nTry again.\n")

##########
# Observed
##########

print("{:<19} {:.2f} substitutions per 100 nucleotides.\n{:19} {:.2f} substitutions per {} nucleotides.\n".format("Observed:", (nuc/seq)*100, "", nuc, int(seq)))

##################
# Hamming distance
##################

hamming = nuc/seq
hammingDistance = hamming * 100
print("{:<19} {:.2f} substitutions per 100 nucleotides.\n{:19} {:.2f} substitutions per {} nucleotides.\n".format("Hamming distance:", hammingDistance, "", hammingDistance*(seq/100), int(seq)))

####################
# Poisson correction
####################

poissonCorrection = -ln(1-hamming)*100 
print("{:<19} {:.2f} substitutions per 100 nucleotides.\n{:19} {:.2f} substitutions per {} nucleotides.\n".format("Poisson correction:", poissonCorrection, "", poissonCorrection*(seq/100), int(seq)))

##################################
# Jukes-Cantor one-paramater model
##################################
if nuc/seq <= 74/100:
    jukesCantor = -3/4*ln(1-4/3*hamming)*100
    print("{:<19} {:.2f} substitutions per 100 nucleotides.\n{:19} {:.2f} substitutions per {} nucleotides.\n".format("Jukes-Cantor:", jukesCantor, "", jukesCantor*(seq/100), int(seq)))
else:
    print("{:<19} {}\n".format("Jukes-Cantor:", "Not possible to calculate."))