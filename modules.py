# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# core modules
import datetime
from datetime import date
from time import time

# PIP module
from camelcase import CamelCase

# Import custom module
import vaildator
from vaildator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello there world'))
email = 'idk@123#'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')
# print(timestamp)