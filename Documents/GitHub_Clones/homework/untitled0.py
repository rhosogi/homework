# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 07:33:14 2015

@author: reneehosogi
"""

import pandas as pd
yelp = pd.read_csv('/Users/reneehosogi/Documents/GitHub_Clones/GA-SEA-DAT1/data/yelp.csv')
yelp.head(1)

import json
with open('/Users/reneehosogi/Documents/GitHub_Clones/GA-SEA-DAT1/data/yelp.json', 'rU') as f:
    data = [json.loads(row) for row in f]
    
header = data.json()[0]
type(header)