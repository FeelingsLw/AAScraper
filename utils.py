# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:31:39 2017

@author: andre
"""

import json
import logging
import os
import re

from collections import defaultdict
from datetime import timedelta
from itertools import tee
from json import JSONDecodeError

log = logging.getLogger(__name__)
local_path = os.path.dirname(__file__)


def daterange(start_date, end_date):
    # Returns all dates between start_date and end_date
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def open_file(file):
    # Attempts to open the a file, and creates the file if it does not exist
    file_dir = os.path.join(local_path, 'data', file)
    try:
        with open(file_dir, 'r') as f:
            data = json.load(f)
            return defaultdict(dict, data)
    except FileNotFoundError:
        with open(file_dir, 'x+') as f:
            log.info(f"Created {file} file")
            return defaultdict(dict, {})
    except JSONDecodeError:
        return defaultdict(dict, {})


def pairs(a):
    # Returns 2 values per iteration [1, 2, 3, 4, ...] -> ([1, 2], [3, 4], ...)
    return zip(a[::2], a[1::2])


def pairwise(iterable):
    # Returns pairs of values from an iterable variable
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def strip(string):
    # Strips all non-numeric chars from a string, returns a float
    return float(re.sub(r'[^\d.]+', "", str(string)))


def _trimString(val):
    return val.lstrip('\r\n ').rstrip('\r\n ')


def trim(val):
    # Trims a HTML string to plaintext
    return _trimString(val).lstrip('\n').rstrip('\n').replace("\n"," ")
