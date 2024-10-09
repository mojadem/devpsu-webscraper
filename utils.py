def filter_listings(listings, filter_args):
    for key in filter_args.keys():
        print(key)
        val = filter_args.get(key)
        print(val)

        if key == "game" or key == "email":
            print("1")
            listings = list(filter(lambda l: l[key].lower() == val, listings))

        if key == "max_price":
            print("2")
            try:
                max_price = float(val)
            except ValueError:
                continue

            listings = list(filter(lambda l: l["price"] <= max_price, listings))

    return listings
