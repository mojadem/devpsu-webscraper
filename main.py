from database import check_for_unsaved_listings, overwrite_saved_listings
from scrape import scrape_listings


listings = scrape_listings()
new_listings = check_for_unsaved_listings(listings)

print(new_listings)

overwrite_saved_listings(listings)
