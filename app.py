import flask

from errors import ScrapingError
from scrape import scrape_listings
from utils import filter_listings

app = flask.Flask(__name__)


@app.route("/")
def index():
    try:
        listings = scrape_listings()
    except ScrapingError:
        return "no data", 500

    args = flask.request.args

    listings = filter_listings(listings, args)

    res = {"listings": listings}
    return res, 200
