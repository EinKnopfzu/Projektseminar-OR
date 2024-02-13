import routes

def reset():
    routes.status_global = {
        "Daten vorverarbeitet": False,
        "Daten vorabgefragt": False,
        "Datenesel erstellt": False,
        "Hauptabfrage TitleAmazon": False,
        "Antwort TitleAmazon": False,
        "Hauptabfrage DescriptionLongShops": False,
        "Datenähnlichkeiten gestartet": False,
        "Datenähnlichkeiten abgeschlossen": False,
        "Antwort DescriptionLongShops": False,
        "Hauptabfrage SalesArgument": False,
        "Antwort SalesArgument": False,
        "Hauptabfrage AmazonBulletPoints": False,
        "Antwort AmazonBulletPoints": False,
        "Hauptabfrage WorthKnowingShop": False,
        "Antwort WorthKnowingShop": False,
        "Hauptabfrage MetaKeywordShop": False,
        "Antwort MetaKeywordShop": False,
        "Hauptabfrage Reprompt": False,
        "Antwort Reprompt": False
    }