# RottenTomatoesScraper
This application allows you to search for the cast and crew of a movie on Rotten Tomatoes. Simply provide the movie title as an argument and the program will construct the appropriate link and return the information. Please note that if the role of a cast member is not listed on Rotten Tomatoes, it will be displayed as "not listed" in the output.

## Usage
```bash
usage: python3 RottenTomatoesScraper.py [-m "movie"] [-u url]

options: 
  -h, --help  show this help message and exit
  -m "movie"  provide the movie name between parenthesis
  -c          cast & crew
  -i          general information
  -u url      provide the url for a Rotten Tomatoes movie page
  -a "actor"  provide the actor name between parenthesis
  -H          hide the title and other redundant information
```

## Restrictions
* The -m, -u and -a options can not be used together.

## Examples

```bash
python3 RottenTomatoesScraper.py -cm "Jurassic Park"
```
This command will automatically construct the link: https://www.rottentomatoes.com/m/jurassic_park and scrape the page for the cast and crew information of "Jurasic Park".

```bash
python3 RottenTomatoesScraper.py -cm "PUSS IN BOOTS: THE LAST WISH"
```
This command will automatically remove any special characters from the title (e.g. ':'), then construct the link: https://www.rottentomatoes.com/m/puss_in_boots_the_last_wish and scrape the page for the cast and crew information of "PUSS IN BOOTS: THE LAST WISH".

```bash
python3 RottenTomatoesScraper.py -cu https://www.rottentomatoes.com/m/shrek
```

This command will scrape the page for the cast and crew information of "SHREK".

```bash
python3 RottenTomatoesScraper.py -im "The Shawshank Redemption" 
```

This command will automatically construct the link: https://www.rottentomatoes.com/m/the_shawshank_redemption" and scrape the page for the general information of "The Shawshank Redemption".

```bash
python RottenTomatoesScraper.py -a "Tom Hanks" 
```

This command will automatically construct the link: "https://www.rottentomatoes.com/celebrity/tom_hanks" and scrape the page to find information about Tom Hanks.

```bash
python RottenTomatoesScraper.py -ciHm "Shark Tale"
```

This command will automatically construct the link: "https://www.rottentomatoes.com/m/shark_tale" and scrape the page for the general information, the cast and the crew of "Shark Tale". The title and additional redundant messages will be excluded from the output.

## Error handling
Please note that if the -m option is used and the provided movie title is not found on Rotten Tomatoes, the program will return an error message and exit the program. Possible reasons include a typo, unusual symbols in the movie title or the movie not being listed on Rotten Tomatoes. 

It is important to note that Rotten Tomatoes does not always follow its own link construction standards and there may be cases where the URLs for certain movies do not match the expected pattern. If this is the case, you can use the -u option to provide the URL yourself. For example, in the case of "SPIDER-MAN: ACROSS THE SPIDER-VERSE", the expected URL would be https://www.rottentomatoes.com/m/spider_man_across_the_spider_verse, which is the case. The expected URL for "SPIDER-MAN" on the other hand would be https://www.rottentomatoes.com/m/spider_man, but it can only be found on https://www.rottentomatoes.com/m/spiderman. 

## Dependencies
This program requires the following python packages: argparse, urllib and bs4.

## Under construction
The following options and functionalities are currently under construction and will be added in future updates:

* -a or --actor: This option will allow the user to specify an actor they are searching for and return some general information.

Please keep in mind that these features are under construction and may not be fully functional at this time.

## Note
This application is for educational and personal use only. Use of this application for any other purposes may violate Rotten Tomatoes' terms of use.