import re

import requests
from bs4 import BeautifulSoup

from errors import ScrapingError


def _decode_email(code):
    r = int(code[:2], 16)
    email = "".join([chr(int(code[i : i + 2], 16) ^ r) for i in range(2, len(code), 2)])
    return email


def scrape_listings():
    res = requests.get(
        "https://onwardstate.com/penn-state-football-student-ticket-exchange/"
    )

    if res.status_code != 200:
        raise ScrapingError

    soup = BeautifulSoup(res.content, "html.parser")

    listings = []

    for l in soup.find_all("p"):
        l = str(l)

        m = re.search('data-cfemail="(.*)"', l)

        if m is None:
            continue

        email = _decode_email(m.group(1))

        m = re.search(r"wants (.*) for a (.*) \(.*\) ticket.", l)

        if m is None:
            continue

        price = m.group(1)
        game = m.group(2)

        listing = {"email": email, "game": game, "price": price}
        listings.append(listing)

    return listings
