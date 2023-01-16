# ProtRefseqRetriever
This application is a command-line tool that allows you to retrieve the refseq proteins corresponding to a list of genes and organisms. The script takes an input CSV file containing the genes and organisms, and writes the corresponding refseq proteins to an output file.

## usage
```bash
usage: python ProtRefseqRetriever.py [-h] -a api -i input -o output [-d delimiter] [-H]

options: 
  -h, --help      show this help message and exit

  -a, --api       NCBI API key

  -i, --input     input CSV file

  -o, --output    output file

  -d, --delimiter specify the delimiter used in the input file (default: comma; options: [comma, colon, semicolon])

  -H              use this option if the input file has a header on line 1

```

## Examples
```bash
python ProtRefseqRetriever.py -a abc123 -i genes_organisms.csv -o refseq_proteins.txt -d semicolon -H
```
This command will retrieve the refseq proteins corresponding to the genes and organisms in the file genes_organisms.csv, using the API key abc123. The output will be written to the file refseq_proteins.txt, the delimiter used in the input file is a semicolon, and the input file has a header on the first line.

## Input file format
The input file should be a CSV file with the following format:
```bash
gene,organism
TP53,Homo sapiens
BRCA1,Homo sapiens
BRCA2,Homo sapiens
ATM,Homo sapiens
APC,Caenorhabditis elegans
EGFR,Homo sapiens
MYC,Homo sapiens
KRAS,Homo sapiens
PTEN,Homo sapiens
P53,Mus musculus
GSTP1,Homo sapiens
CASP3,Homo sapiens
UBC,Saccharomyces cerevisiae
MDM2,Rattus norvegicus
```

## Notes
* The script requires a valid NCBI API key to function.
* Make sure that the input file is in the correct format and the delimiter specified matches the one used in the file.
* The output file will be overwritten if it already exists.
* The script is tested with Python 3.x and above.

## Acknowledgements
The basic idea for this script was inspired by an example question of the Python Scripting exam from 2018-2019 written by Paco Hulpiau. However, the current script has been developed further and contains additional functionality and error handling. The script uses the [NCBI protein database](https://www.ncbi.nlm.nih.gov/protein/) to retrieve the refseq proteins and the [Entrez Programming Utilities](https://www.ncbi.nlm.nih.gov/books/NBK25499/) to interact with the NCBI database.

