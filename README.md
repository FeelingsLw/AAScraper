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
                "flights": [
                    {
                        "destination": "14:50 (ICN)",
                        "origin": "07:20 (KUL)"
                    }
                ],
                "price": "699.00 MYR"
            },
            {
                "flights": [
                    {
                        "destination": "08:05 (DMK)",
                        "origin": "06:55 (KUL)"
                    },
                    {
                        "destination": "23:05 (ICN)",
                        "origin": "15:40 (DMK)"
                    }
                ],
                "price": "1,953.72 MYR"
            },
...
            {
                "flights": [
                    {
                        "destination": "15:10 (DMK)",
                        "origin": "11:20 (ICN)"
                    },
                    {
                        "destination": "00:15 (KUL) +1",
                        "origin": "21:00 (DMK)"
                    }
                ],
                "price": "1,237.75 MYR"
            }
        ]
    }
}
```