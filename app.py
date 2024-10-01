import flask

from errors import ScrapingError
from scrape import scrape_listings

app = flask.Flask(__name__)


@app.route("/")
def index():
    try:
        listings = scrape_listings()
        res = {"listings": listings}
        return res, 200
    except ScrapingError:
        return "no data", 500
