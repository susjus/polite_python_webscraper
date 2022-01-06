"""requests_example.py"""

import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text[0:269])
