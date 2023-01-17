# TopTunesScraper
This python application scrapes the "bilboard hot 100" page and returns the top selected amount of songs.

## usage
```bash
usage: TopTunesScraper.py [-h] [-o output] [-n amount]

options:
  -h, --help  show this help message and exit
  -o output   output file
  -n amount   amount of top tunes (default: 10)

```

## Restrictions
* The value of the -n argument must be between 1 and 100. If not specified, the default value is 10.

## Examples
```bash
python TopTunesScraper.py -o top10.txt
```
This command will retrieve the top 10 songs and save them in a file named "top10.txt".

```bash
python TopTunesScraper.py -n 50
```
This command will retrieve the top 50 songs and print them in the terminal.

```bash
python TopTunesScraper.py -o top100.txt -n 100
```
This command will retrieve the top 100 songs and save them in a file named "top100.txt".

## Notes
* The application might not work properly if the website's structure is changed.
* The information from the website is subject to change and might not be up to date.
* This application is for educational and personal use only. Use of this application for any other purposes may violate billboard's terms of use.

