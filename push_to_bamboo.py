from pybamboo.connection import Connection
from pybamboo.dataset import Dataset
import os
import simplejson as json

with open('bamboo_hash.json','r') as f:
  hash_json = json.loads(f.read())


#Education_Facilities.csv  Education_LGA.csv  Health_Facilities.csv  Health_LGA.csv  Makefile  Water_Facilities.csv  Water_LGA.csv
