# AAScraper

![Python 3.2](https://img.shields.io/badge/python-3.2-blue.svg)

AAScraper is a web scraper tool that scrapes the AirAsia booking website to organically obtain the prices of all and the cheapest flights for a given date range, inspired by SkyScanner. 

### Installation

AAScraper uses a number of open source Python libraries to work properly.

* `bs4` - Beautiful Soup 4 to parse the HTML source(s)
* `requests` and `urllib` to perform the requests

For installation run the command:
```sh
$ pip3 install requirements.txt
```

### Usage

Included with the source is the file `scrape.py` that gives an example on how these functions are meant to be used. The function `scrape()` creates a file with the cheapest outgoing and return flights for every single day in a given date range.

Example output:
```json
{
    "2017-12-12": {
        "outgoing": [
            {