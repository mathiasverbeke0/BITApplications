# RottenTomatoesScraper
This application allows you to search for the cast and crew of a movie on Rotten Tomatoes. Simply provide the movie title as an argument and the program will construct the appropriate link and return the information. Please note that if the role of a cast member is not listed on Rotten Tomatoes, it will be displayed as "not listed" in the output.

## usage
```bash
usage: python3 movie_scraper.py -m "movie"

options: 
  -h, --help    show this help message and exit
```

## Examples
Let's say you want to find the cast and crew of the movie "Jurassic Park". To do this, you would run the following command:

```bash
python3 RottenTomatoesScraper.py -m "Jurassic Park"
```

The program will then construct the link: https://www.rottentomatoes.com/m/jurassic_park and scrape the page for the cast and crew information. The output will display the main cast and crew members.

```bash
 ______     ______     ______   ______   ______     __   __        ______   ______     __    __     ______     ______   ______     ______     ______    
/\  == \   /\  __ \   /\__  _\ /\__  _\ /\  ___\   /\ '-.\ \      /\__  _\ /\  __ \   /\ '-./  \   /\  __ \   /\__  _\ /\  __ \   /\  ___\   /\  ___\   
\ \  __<   \ \ \/\ \  \/_/\ \/ \/_/\ \/ \ \  __\   \ \ \-.  \     \/_/\ \/ \ \ \/\ \  \ \ \-./\ \  \ \  __ \  \/_/\ \/ \ \ \/\ \  \ \  __\   \ \___  \  
 \ \_\ \_\  \ \_____\    \ \_\    \ \_\  \ \_____\  \ \_\'\_\       .\ \_\  \ \_____\  \ \_\ \ \_\  \ \_\ \_\    \ \_\  \ \_____\  \ \_____\  \/\_____\ 
  \/_/ /_/   \/_____/     \/_/     \/_/   \/_____/   \/_/ \/_/        \/_/   \/_____/   \/_/  \/_/   \/_/\/_/     \/_/   \/_____/   \/_____/   \/_____/ 
 
The link 'https://www.rottentomatoes.com/m/jurassic_park' will be used to search for the data.

Connecting to Rotten Tomatoes ...

Cast:
-----
- Sam Neill as Dr. Alan Grant
- Laura Dern as Dr. Ellie Sattler
- Jeff Goldblum as Dr. Ian Malcolm
- Richard Attenborough as John Hammond
- Bob Peck as Robert Muldoon
- Martin Ferrero as Donald Gennaro
- BD Wong as Chief Geneticist Dr. Henry Wu
- Joseph Mazzello as Tim Murphy
- Ariana Richards as Alexis "Lex" Murphy
- Samuel L. Jackson as Ray Arnold
- Wayne Knight as Dennis Nedry

Crew:
-----
- Director: Steven Spielberg
- Writer: Michael Crichton
- Screenwriter: Michael Crichton
- Screenwriter: David Koepp
- Screenwriter: Malia Scotch Marmo
- Producer: Kathleen Kennedy
- Producer: Gerald R. Molen
- Associate Producer: Lata Ryan
- Associate Producer: Colin Wilson
- Original Music: John Williams
- Cinematographer: Dean Cundey
- Film Editing: Michael Kahn
- Film Editing: Steven Spielberg
- Casting: Janet Hirshenson
- Casting: Jane Jenkins
- Production Design: Rick Carter
- Art Director: John Bell
- Art Director: William James Teegarden
- Set Decoration: Jackie Carr
- Makeup Artist: Christina Smith
```

Let's say you want to find the cast and crew of the movie "PUSS IN BOOTS: THE LAST WISH". To do this, you would run the following command:

```bash
python3 RottenTomatoesScraper.py -m "Jurassic Park"
```

The program will automatically remove any special characters such as ":" and construct the link: https://www.rottentomatoes.com/m/puss_in_boots_the_last_wish and scrape the page for the cast and crew information. The output will display the main cast and crew members.

## Error handling
In case the provided movie title is not found on Rotten Tomatoes, the program will return an error message and exit the program.

## Dependencies
This program requires the following python packages: argparse, urllib and bs4.

## Note
This application is for educational and personal use only. Use of this application for any other purposes may violate Rotten Tomatoes' terms of use.