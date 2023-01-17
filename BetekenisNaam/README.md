# BetekenisNaam
Dit python script geeft de betekenis van je naam als je deze invoert. Het script haalt de betekenis van de website "[Betekenis namen](https://www.betekenisnamen.nl/)".

## usage
```bash
usage: BetekenisNaam.py [-h] -n naam

options:
  -h, --help  show this help message and exit
  -n naam     naam waarvan je de betekenis wil opzoeken

```

## Restricties
* Namen met niet-alfabetische symbolen zullen een foutmelding genereren.

## Examples
```bash
python BetekenisNaam.py -n Jeroen
```
Dit commando wordt gebruikt om de betekenis van de naam "Jeroen" op te zoeken.

```bash
python BetekenisNaam.py -n Sophie
```
Dit commando wordt gebruikt om de betekenis van de naam "Sophie" op te zoeken.

## Notes
* Het script kan alleen namen geven die op de website "[Betekenis namen](https://www.betekenisnamen.nl/)" zijn opgenomen. Als de naam die je opgeeft niet op de website zit, zal het script geen betekenis geven.
* Deze toepassing is alleen voor educatieve en persoonlijke doeleinden. Gebruik van deze toepassing voor andere doeleinden kan in strijd zijn met de gebruiksvoorwaarden van de website.

