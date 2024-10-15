import flask

from database import check_for_unsaved_listings, overwrite_saved_listings
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


@app.route("/update", methods=["POST"])
def update():
    try:
        listings = scrape_listings()
    except ScrapingError:
        return "no data", 500

    unsaved_listings = check_for_unsaved_listings(listings)

    overwrite_saved_listings(listings)

    res = {"newListings": unsaved_listings}
    return res, 200
