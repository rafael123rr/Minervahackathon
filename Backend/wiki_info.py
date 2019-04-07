import wikipedia


def get_info(page_name): # take string page_name, returns dictionary with info
    res = {}
    try:
        page = wikipedia.page(page_name)
    except:
        return None
    res["summary"] = page.summary

    try:
        res["health"] = page.section("Health")
    except:
        res["health"] = "no health data available"
    return res


def format(dict):
    for thing in dict:
        print(thing + ":")
        print(dict[thing])


if __name__ == "__main__":
    print(get_info("iron"))
