# DisComics
This application allows you to search for comics that are in discount on bol.com.

## Usage
```bash
usage: DisComics.py [-h] [-d] [-m] [-c CHAR] [-a] [-s]

options:
  -h, --help            show this help message and exit
  -d, --DC              DC comics
  -m, --marvel          marvel comics
  -c char, --char char  specific character
  -a, --all             all comics
  -s, --show            show all pages
```

## Restrictions
* The -m, -d and -a options can not be used together.

## Examples

```bash
python DisComics.py -m
```
This command will show you the first page of marvel comics that are in discount on bol.com.

```bash
python DisComics.py -m -c spider-man
```
This command will show you the first page of marvel comics about spider-man that are in discount on bol.com.

```bash
python DisComics.py -s -c "black panther"
```
This command will show you all comics about black panther that are in discount on bol.com.

```bash
python3 RottenTomatoesScraper.py -a -s 
```
This command will show you all comics that are in discount on bol.com.

## Under construction
There is a still a bug in the application that can mess up the information of a complete page. If the price of a comic on bol.com equals 'niet-leverbaar', the application will display that the information of an entire page can not be showed (this is intentional).  

## Note
This application is for educational and personal use only. Use of this application for any other purposes may violate bol.com's terms of use.