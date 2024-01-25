# check_structures.py

def check_sales_argument_structure(response_text):
    return (response_text.startswith(("<ul><li>", "<ul>\n<li>"))
            and (response_text.count("</li><li>") + response_text.count("</li>\n<li>") == 4)
            and response_text.endswith(("</li></ul>", "</li>\n</ul>")))

def check_structure(key, response_text):
    if key == 'SalesArgument':
        return check_sales_argument_structure(response_text)


