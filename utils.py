def filter_listings(listings, filter_args):
    for key in filter_args.keys():
        val = filter_args.get(key)

        if key == "game" or key == "email":
            listings = list(filter(lambda l: l[key].lower() == val, listings))

        if key == "max_price":
            try:
                max_price = float(val)
            except ValueError:
                continue

            listings = list(filter(lambda l: l["price"] <= max_price, listings))

    return listings
