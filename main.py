import random, string, cloudscraper, configparser

import requests
import time

scraper = cloudscraper.create_scraper()

config = configparser.ConfigParser()
config.read('config.ini')
cmain = config["main"]
domain = cmain["domain"]
lngth = int(cmain["length"])

new = 1

tic = time.perf_counter()
found = 0
while found == 0:
    id = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=lngth))
    URL = f"https://{domain}/raw/" + str(id)
    print(URL)
    r = requests.get(URL)
    print(r)
    if r.status_code == 404:
        print("Didn't found, trying again")
        continue
    page = scraper.get(URL)
    print(page)
    file = open('notatniczek.txt', 'w', encoding='utf-8')
    file.write(page)
    file.close()


