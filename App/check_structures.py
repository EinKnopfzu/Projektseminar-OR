# check_structures.py



def check_length(key, response_text, i):
    if key == 'DescriptionLongShops':
        if i == 0:
            return 400 <= (len(response_text) - len("<h2>") - len("</h2><p>") - len("</p>")) <= 550
        elif i == 1:
            return 300 <= (len(response_text) - len("<h2>") - len("</h2><p>") - len("</p>")) <= 650
        else:
            return True
    else:
        return True



def check_html(key, response_text):
    if key == 'SalesArgument':
        return (response_text.startswith(("<ul><li>", "<ul>\n<li>"))
            and (response_text.count("</li><li>") + response_text.count("</li>\n<li>") == 4)
            and response_text.endswith(("</li></ul>", "</li>\n</ul>")))
    if key == 'WorthKnowingShop':
        return (response_text.startswith("<h2>")
            and ("</h2><ul><li>" in response_text)
            and (response_text.count("</li><li>") == 5)
            and (response_text.endswith("</li></ul>")))
    if key == 'DescriptionLongShops':
        return ((response_text.startswith("<h2>"))
            and ("</h2><p>" in response_text)
            and (response_text.endswith("</p>")))
