import requests
from bs4 import BeautifulSoup

import re
import json


def decode_email(code):
    r = int(code[:2], 16)
    email = "".join([chr(int(code[i : i + 2], 16) ^ r) for i in range(2, len(code), 2)])
    return email


res = requests.get(
    "https://onwardstate.com/penn-state-football-student-ticket-exchange/"
)

print(res.status_code)

assert res.status_code == 200

soup = BeautifulSoup(res.content, "html.parser")

listings = []

for l in soup.find_all("p"):
    l = str(l)

    m = re.search('data-cfemail="(.*)"', l)

    if m is None:
        continue

    email = decode_email(m.group(1))

    m = re.search(r"wants (.*) for a (.*) \(.*\) ticket.", l)

    assert m is not None

    price = m.group(1)
    game = m.group(2)

    listing = {"email": email, "game": game, "price": price}
    listings.append(listing)

saved_listings = set()

try:
    with open("listings.txt") as f:
        for line in f.readlines():
            saved_listings.add(line.strip())
except FileNotFoundError:
    print("no saved listings")

for l in listings:
    serialized_l = json.dumps(l, sort_keys=True)

    if serialized_l not in saved_listings:
        print(l["game"], l["price"], l["email"])

with open("listings.txt", "w") as f:
    serialized_listings = map(lambda l: f"{json.dumps(l, sort_keys=True)}\n", listings)
    f.writelines(serialized_listings)
