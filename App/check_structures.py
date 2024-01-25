# check_structures.py

def check_sales_argument_structure(response_text):
    return (response_text.startswith(("<ul><li>", "<ul>\n<li>"))
            and (response_text.count("</li><li>") + response_text.count("</li>\n<li>") == 4)
            and response_text.endswith(("</li></ul>", "</li>\n</ul>")))
    
def check_worth_knowing_shop_structure(response_text):
    return (response_text.startswith("<h2>")
            and ("</h2><ul><li>" in response_text)
            and (response_text.count("</li><li>") == 5)
            and (response_text.endswith("</li></ul>")))

def check_description_long_shops_structure(response_text):
    return (response_text.startswith("<h2>")
            and ("</h2><p>" in response_text)
            and (response_text.endswith("</p>")))

def check_structure(key, response_text):
    if key == 'SalesArgument':
        return check_sales_argument_structure(response_text)
    if key == 'WorthKnowingShop':
        return check_worth_knowing_shop_structure(response_text)
    if key == 'DescriptionLongShops':
        return check_description_long_shops_structure(response_text)
