#!/usr/bin/python3

#########################################################################################
# Author: Mathias Verbeke
# Date of creation: 2022/01/09
# Usage: This script interprets PAM Log-Odds scores in the context of pairwise alignment.
# Input: A Log-Odds score or a file with comma separated Log-Odds scores
# Output: The interpretation of the Log-Odds score
#########################################################################################

##################
# Imported modules
##################

import argparse, sys, os, csv

#######################
# Constructed functions
#######################

def LogOdds(score, flag):
    # Transformation of the Log-Odds score
    relatednessOdds = 10**(score/10)

    # Assignment of an interpretation
    if relatednessOdds < 1:
        freq = round(1/relatednessOdds,2)

        if flag == "single":
            result = "It is likely that the alignment of the two amino acids is due to chance, rather than them being actual homologues.\nThis likelihood is {} times greater than the probability that the amino acids are homologues.".format(freq)
        
        elif flag == "multi":
            result = "AA alignment due to: chance\t\t\t\t\tLikelihood: {} times more likely".format(freq)
        
    elif relatednessOdds == 1:
        if flag == "single":
            result = "The alignment of the two amino acids could be due to either chance or homology.\nBoth possibilities are equally likely."

        elif flag == "multi":
            result = "AA alignment due to: homology or chance\t\tLikelihood: equally likely"

    elif relatednessOdds > 1:
        if flag == "single":
            result = "It is likely that the alignment of the two amino acids is due to the fact that they are homologues, rather than the alignment occurring by chance.\nThis likelihood is {} times greater than the probability that the alignment occurred by chance.".format(round(relatednessOdds, 2))
        
        elif flag == "multi":
            result = "AA alignment due to: homology\t\t\t\tLikelihood: {} times more likely".format(round(relatednessOdds, 2))

    return result

##################
# Parsed arguments
##################

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--score', metavar = 'score', type = float, required = False, help = 'provide a Log-Odds score that you want to interpret')
parser.add_argument('-i', '--input', metavar = 'input', required= False, help= 'an input file with Log-Odds scores on seperate lines')
parser.add_argument('-o', '--output', metavar = 'output', required = False, help = 'an output file for the Log-Odds interpretations')
parser.add_argument('-n', '--newline', required = False, action = 'store_true', help = 'place a newline in the output file for every line of Log-Odd scores in the input file')

args = parser.parse_args()

#################
# Argument checks
#################

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()

elif (args.input == None and args.output != None) or (args.input != None and args.output == None):
    sys.exit("Error: -i and -o can not be used seperatly!")

elif args.score != None and (args.input != None or args.output != None):
    sys.exit("Error: You can use -i and -o together or you can use -s seperately. You can't combine all 3. Make up your mind!")

elif args.score != None and args.newline != False:
    sys.exit("Error: -s and -n can not be used together!")

if args.input != None:
    if not os.path.exists(args.input):
        sys.exit("Error: The input file does not exist.")
    
if args.output != None:
    while os.path.exists(args.output):
        
        warning = input("WARNING: {} already exists on the specified location. Do you want to override this file? [y/n] ".format(os.path.basename(args.output)))

        if warning in ["y", "Y", "yes", "Yes", "YES"]:
            break

        elif warning in ["n", "N", "no", "No", "NO"]:
            while True:

                question = input("Do you want to write the output to another output file? [y/n] ")

                if question in ["y", "Y", "yes", "Yes", "YES"]:
                    new = input("Provide the new output file: ")
                    args.output = new
                    break
                
                elif question in ["n", "N", "no", "No", "NO"]:
                    sys.exit()

                else:
                    print("Invalid respons, try again!")

        else:
            print("Invalid response, try again!")

###########
# Execution
###########

# Interpretation of a single score
if args.score != None:
    score = args.score
    flag = "single"

    print("{}".format(LogOdds(score, flag)))

# Interpretation of multiple scores from an input file
if args.input != None and args.output != None:
    flag = "multi"
    
    input, output = args.input, args.output

    outputFile = open(output, "w")

    inputFile = open(input, "r")
    csv_reader = csv.reader(inputFile, delimiter =',')

    for line in csv_reader:
        for score in line:
            score.strip()

            # Throw error in case a score value can not be changed to a float
            try:
                score = float(score)

            except Exception as e:
                print(e)
                print("The scores in {} were interpreted and placed in {} up to the point of the score that throws an error.".format(os.path.basename(input), os.path.basename(output)))
                inputFile.close()
                outputFile.close()
                sys.exit()
            
            outputFile.write("Score: {:<10.2f}\t{}\n".format(score, LogOdds(score, flag)))
        
        if args.newline == True:
            outputFile.write("\n")

    inputFile.close()
    outputFile.close()