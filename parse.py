# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:40:18 2017

@author: andre
"""

import requests
import urllib

from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from utils import strip, pairs, trim

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) ' +
                         'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                         'Chrome/50.0.2661.102 Safari/537.36'}

headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

search_url = 'https://booking.airasia.com/Flight/Select?'


def cheapest(list):
    # Returns the a list cheapest flights from a list of flights
    min_price = min(strip(trip['price']) for trip in list)
    cheapest_trips = [x for x in list if strip(x['price']) == min_price]
    return cheapest_trips


def price_from_containers(containers):
    # Given javascript containers, parses all the prices in each container.
    for container in containers:
        raw_prices = container.find_all('div', {"class":"avail-fare-price"})
        prices = [float(strip(price)) for price in raw_prices]
        yield prices


def parse_prices(html_source):
    # Returns all departing and returning flight prices in html_source
    soup = BeautifulSoup(html_source, 'lxml')
    containers = soup.find_all('div', {'class': 'js_availability_container'})
    depart_list, return_list = parse_containers(containers)
    return depart_list, return_list


def parse_containers(containers):
    # Parse an AirAsia price container and returns a list of flights
    for container in containers:
        rows = container.findAll('tr', {'class': ['fare-light-row', 
                                                  'fare-dark-row']})
        list_of_flights = []
        for row in rows:
            rowOfFare = row.findAll('tr', {'class': ['fare-light-row', 
                                                     'fare-dark-row']})
            trip = {}
            if len(rowOfFare) > 0:
                flights = row.findAll('td', {'class': 'avail-table-detail'})
                for depart, arrive in pairs(flights):
                    d, a = trim(depart.getText()), trim(arrive.getText())
                    flight = {'origin': f'{d}', 'destination': f'{a}'}
                    trip.setdefault('flights', []).append(flight)
                price = row.findAll('div', {'class': 'avail-fare-price'})[0].getText()
                trip['price'] = trim(price)
                list_of_flights.append(trip)
        yield list_of_flights


def search_flight(destination, depart_date, return_date, params):
    # Returns all departing and returning flight for the given parameters
    params['d1'] = destination
    params['dd1'] = depart_date
    params['dd2'] = return_date
    parsed_params = urllib.parse.urlencode(params)
    with requests.Session() as s:
        retries = Retry(backoff_factor=5, status_forcelist=[403, 502, 503, 504])
        s.mount('https://', HTTPAdapter(max_retries=retries))
        s.get("https://booking.airasia.com/", headers=headers2)
        response = s.get(search_url + parsed_params, headers=headers2)
    outgoing_list, return_list = parse_prices(response.content)
    return outgoing_list, return_list
