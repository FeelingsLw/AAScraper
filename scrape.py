# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 02:14:09 2017

@author: andre
"""

import json
import logging

from datetime import date

from utils import daterange, open_file, pairwise
from parse import get_lowest_prices, search_flight

# SEARCH PARAMS
origin = 'KUL'
destination = 'ICN'
depart_date = '2017-12-12'
return_date = '2017-12-15'
adults = '1'
childs = '0'
currency = 'MYR'

params = {'o1' : origin,
          'd1' : destination,
          'dd1' : depart_date,
          'dd2' : return_date,
          'r' : 'true',
          'ADT' : adults,
          'CHD' : childs,
          'inl' : 0, 
          's' : 'true',
          'mon' : 'true',
          'cc' : currency}

# INITIALISE LOGGER
fmt = "[%(asctime)s] [%(levelname)8s] --- %(message)s"
datefmt = "%Y/%m/%d %H:%M:%S"
logging.basicConfig(level=logging.INFO, format=fmt, datefmt=datefmt)
log = logging.getLogger(__name__)

log.info("Logger initialised")

# INPUTS
start_date = date(2017, 12, 1)
end_date = date(2017, 12, 5)
origin = 'KUL'
destination = 'ICN'

def scrape(origin, destination, start_date, end_date):
    # Creates a file with the cheapest outgoing and return flights for a given
    # date range.
    items = int((end_date - start_date).days) - 1
    date_list = daterange(start_date, end_date)
    
    data = {}
    
    for index, (depart_date, return_date) in enumerate(pairwise(date_list)):
        try:
            depart_list, return_list = search_flight(destination, 
                                                         depart_date, 
                                                         return_date, 
                                                         params)
        except: 
            log.error(f"Some error occured, retrying item {index+1}/{items}")
        data = open_file(f'{destination}.json')
        data[str(depart_date)]['outgoing'] = min_depart
        data[str(return_date)]['return'] = min_return
        with open(f'{destination}.json', 'w') as f:
            json.dump(data, f, sort_keys=True, indent=8, separators=(',', ': '))
        log.info(f"Search {index+1}/{items} complete: {depart_date} to "
                 f"{return_date}. ({min_depart}MYR, {min_return}MYR)")

scrape(origin, destination, start_date, end_date)