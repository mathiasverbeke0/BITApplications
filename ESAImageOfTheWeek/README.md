# ESAImageOfTheWeek
This application allows you to search download the "[Earth observation of the week](https://www.esa.int/ESA_Multimedia/Sets/Earth_observation_image_of_the_week/(result_type)/images)" image from ESA. 

## Usage
```bash
usage: ESAImageOfTheWeek.py [-h] [-d directory]

options:
  -h, --help    show this help message and exit
  -d directory  directory where you want to store the picture
```

## Examples

```bash
python3 ESAImageOfTheWeek.py
```
This command will download the latest "Earth observation of the week" image in your present working directory.

```bash
python3 ESAImageOfTheWeek.py -d /home/mathias/ESAImages
```
This command will download the latest "Earth observation of the week" image in the ESAImages folder.

## Note
This application is for educational and personal use only. Use of this application for any other purposes may violate ESA's terms of use.