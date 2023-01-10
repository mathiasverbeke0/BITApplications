# LogOddsInterpreter

This application interprets PAM Log-Odds scores in the context of pairwise alignments.

## Usage

```bash
usage: LogOddsInterpreter.py [-h] [-s score] [-i input] [-o output] [-n]

options:
  -h, --help            show this help message and exit
  -s score, --score score
                        provide a Log-Odds score that you want to interpret
  -i input, --input input
                        an input file with Log-Odds scores on seperate lines
  -o output, --output output
                        an output file for the Log-Odds interpretations
  -n, --newline         place a newline in the output file for every line of Log-Odd scores in the input file
```

## Examples
### Interpreting a single Log-Odds score

To interpret a single Log-Odds score, use the -s or --score option followed by the score:

```bash
$ python LogOddsInterpreter.py -s 8.5
```

### Interpreting multiple Log-Odds scores from an input file

To interpret multiple Log-Odds scores from an input file, use the -i or --input option followed by the path to the input file. Additionally, use the -o or --output option followed by the path to the output file to save the interpretations to a file:

```bash
$ python LogOddsInterpreter.py -i scores.txt -o interpretations.txt
```

You can also use the -n or --newline option to include a newline in the output file for every line of Log-Odds scores in the input file:

```bash
$ python LogOddsInterpreter.py -i scores.txt -o interpretations.txt -n
```