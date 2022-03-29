import pandas as pd

import requests

r = requests.get('http://google.com')

d = r.text

print(d)