"""
In diesem File werden die Prompts bzw. Prompt Teile für die Abfragen verwaltet!
Bei User Prompts mit Part1 und Part2 werden die Daten zwischen die beiden Parts gefügt.
#######################################################################################################################################################################################################
"""
"""
Prompt 1 - Generate Product Features
    -> Vorabfrage um einen Datenesel aufzubauen
    -> wird 3x ausgeführt
"""
pre_system_prompt_1 = "Du bist ein Spezialist für E-Commerce und SEO. Du hast Expertise im Extrahieren und Abstrahieren von Produktmerkmalen, welche entscheidend für die Kaufentscheidung sind, welche helfen, die Vorzüge eines Produktes zu erkennen, und welche die Benutzererfahrung hervorheben. Du arbeitest marketing- und zielgruppenorientiert. Du antwortest immer in folgendem Format: 'Produktmerkmal 1 / Produktmerkmal 2 / [...] / Produktmerkmal x'."
pre_user_prompt_1_part1 = "Extrahiere und abstrahiere ca. 10 Produktmerkmale anhand der folgenden Produktdaten:\n\n"
pre_user_prompt_1_part2 = "\n\nIdentifiziere attraktive, verkaufsfördernde Merkmale, die für diese Produktart typisch sind, ohne jedoch spezifische Funktionen oder Eigenschaften zu erfinden, die nicht im Datensatz erwähnt werden. Stelle sicher, dass die Merkmale zwar einer subjektiven, positiven Beurteilung ähneln, aber realistisch und in Übereinstimmung mit den gegebenen Produktdaten sind. Vermeide übertriebene Annahmen oder Ergänzungen, die kaum aus den gegebenen Informationen abgeleitet werden können.\n\nAntworte im Format 'Produktmerkmal 1 / Produktmerkmal 2 / ... / Produktmerkmal x'."

"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 2 - Refine Product Features
    -> Vorabfrage um einen Datenesel aufzubauen
    -> wird 1x ausgeführt und kombiniert die 3 erzeugten Prompt zu einem
"""
pre_system_prompt_2 = "Du bist ein Spezialist für E-Commerce und SEO. Du hast Expertise im Extrahieren und Abstrahieren von Produktmerkmalen, welche entscheidend für die Kaufentscheidung sind, welche helfen, die Vorzüge eines Produktes zu erkennen, und welche die Benutzererfahrung hervorheben. Du arbeitest marketing- und zielgruppenorientiert. Du antwortest immer in folgendem Format: 'Produktmerkmal 1 / Produktmerkmal 2 / [...] / Produktmerkmal x'."
pre_user_prompt_2_part1 = "Extrahiere ca. 10 Produktmerkmale aus den folgenden Produktmerkmalen:\n\n"
pre_user_prompt_2_part2 = "\n\nIdentifiziere attraktive, verkaufsfördernde Merkmale, die für diese Produktart typisch sind. Stelle sicher, dass die Merkmale einer subjektiven, positiven Beurteilung ähneln, wie z.B. 'stilvolles Design', 'hoher Komfort' oder 'benutzerfreundliche Handhabung'. Entferne bzw. ignoriere Merkmale, die objektiverer Natur sind und sich oft in Zahlen ausdrücken, wie z.B. '3m breit' oder '40 Stück in rot und blau'. Unerwünschte Merkmale sind hier oft solche, die sich auf einem Produktdatenblatt wiederfinden würden. Du kannst objektive, spezifische Produktdetails durch beschreibende Adjektive ersetzen, die die Qualität, Funktionalität oder das Erscheinungsbild des Produkts beschreiben, wie z.B. 'leicht', 'robust' oder 'elegant'. Berücksichtige die Zielgruppe und den vorgesehenen Verwendungszweck des Produkts bei der Auswahl der Merkmale, wenn deutlich wird, um was für ein Produkt es sich handelt. Wähle Merkmale, die für potenzielle Käufer am ansprechendsten und relevantesten sind. Vermeide sehr übertriebene Aussagen.\n\nAntworte im Format 'Produktmerkmal 1 / Produktmerkmal 2 / ... / Produktmerkmal x'."


"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 1 - Hauptprompt AmazonTitle
    -> Ziel ist es einen guten AmazonTitle zu generieren
"""
system_prompt_1 = "Du bist ein erfahrener und erfolgreicher Redakteur im Contentteam von Relaxdays. Relaxdays hat sich auf den Online-Verkauf von Produkten in den Bereichen Haus, Garten und Freizeit spezialisiert. Die Produkte des Unternehmens werden über einen eigenen Webshop sowie über verschiedene Online-Plattformen an Kunden in ganz Europa vertrieben."
user_prompt_1 = "Generiere einen prägnanten Titel für das Produkt, der für den Verkauf auf dem Amazon-Marktplatz optimiert ist. Der Titel sollte: maximal 120 Zeichen umfassen; einige Keywords enthalten, und Farbe, Größe, Material und Einsatzgebiet des Produktes beschreiben. Jetzt folgen die Daten: "

"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 2 - Hauptprompt DescriptionLongShops
    -> Ziel ist es einen guten DescriptionLongShops zu generieren
"""
system_prompt_2 = "Du bist ein erfahrener und erfolgreicher Redakteur im Contentteam von Relaxdays. Relaxdays hat sich auf den Online-Verkauf von Produkten in den Bereichen Haus, Garten und Freizeit spezialisiert. Die Produkte des Unternehmens werden über einen eigenen Webshop sowie über verschiedene Online-Plattformen an Kunden in ganz Europa vertrieben."
user_prompt_2 = "Generiere einen DescriptionLongShops. Jetzt folgen die Daten: "

"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 3 - Hauptprompt SalesArguments
    -> Ziel ist es einen guten SalesArguments zu generieren
"""
system_prompt_3 = "Du bist ein erfahrener und erfolgreicher Redakteur im Contentteam von Relaxdays. Relaxdays hat sich auf den Online-Verkauf von Produkten in den Bereichen Haus, Garten und Freizeit spezialisiert. Die Produkte des Unternehmens werden über einen eigenen Webshop sowie über verschiedene Online-Plattformen an Kunden in ganz Europa vertrieben."
user_prompt_3 = """Deine Herausforderung besteht darin, „Sales Argumente“ für einen neuen Artikel basierend auf den folgenden vorliegenden Produktdaten zu erstellen. 
Du sollst nur die Sales Argumente generieren, also auf zusätzliche Umschreibungen, Stichpunkte, usw. verzichten.
Du solltest dich an folgender Anleitung sorgfältig orientieren:
Produktinformationen erfassen:
<<DescriptionLongShops>>
... alternative Attribute ausprobieren
Merkmale hervorheben
Zusätzliche Informationen integrieren
Zielgruppenansprache und Stil interpretieren und integrieren
Suchmaschinenoptimierte Begriffe identifizieren und integrieren
Finale Erstellung der Sales Argumente
Die Sales Argumente müssen, wie in nachfolgenden Beispielen illustriert, immer fünf sein, mit HTML-Tags genauso markiert werden, und sollten sehr kurz, „stichpunktartig“ geschrieben sein.
Jetzt folgen die Daten: """
"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 4 - Hauptprompt AmazonBulletPoints
    -> Ziel ist es einen guten AmazonBulletPoints zu generieren
"""
system_prompt_4 = "Du bist ein erfahrener und erfolgreicher Redakteur im Contentteam von Relaxdays. Relaxdays hat sich auf den Online-Verkauf von Produkten in den Bereichen Haus, Garten und Freizeit spezialisiert. Die Produkte des Unternehmens werden über einen eigenen Webshop sowie über verschiedene Online-Plattformen an Kunden in ganz Europa vertrieben."
user_prompt_4 = """Deine Herausforderung besteht nun darin, 5 Bullet Points für den Marktplatz von amazon zu generieren. Geh bei der folgenden Anleitung bitte sorgfältig und Schritt für Schritt vor.
1.Es sollen 5 Stichpunkte erstellt werden
2.Die einzelnen Stichpunkte dürfen eine Länge von 160 Zeichen unter gar keinen Umständen überschreiten
3. Prüfe nochmals, ob die zulässige Länge auch nicht überschritten wurde, diese ist ein KO-Kriterium.
4..Es soll ein maximaler Wissenstransfer für die gegebene Zeichenlänge stattfinden
Nun folgen weitere semantische Anforderungen, atme tief durch und gehe auch hier Schritt für Schritt vor.
1.Die Bullet Points sollen kundenzentriert formuliert werden, das heißt, dass eine starre Aneinanderreihung von Produkteigenschaften unerwünscht ist.
2.Die Bullet Points werden so angeordnet, dass die relevantesten Eigenschaften zuerst erwähnt werden, es findet dabei also eine Priorisierung nach unten statt.
3.Keywords in den Bullet Points dürfen nicht doppelt verwendet werden, ebenso sind Synonyme nach bestem Gewissen zu vermeiden
Für die weitere Optimierung sind noch folgende Fragen zu beachten, die sich in den Punkten wiederfinden müssen: Welche Vorteile bringt das Produkt für den Kunden? Warum sollte sich der Kunde für genau dieses Produkt entscheiden? Was hat das Produkt für einen Vorteil gegenüber konkurrierenden Produkten?
Der Kundennutzen hat eine höhere Priorität als das Produktfeature. Achte also zuerst auf den Kundennutzen, bevor das Produktfeature erwähnt wird.Es dürfen auch vereinzelt Magic Words erwähnt werden, die Bilder und Emotionen im Kopf wecken.
Erstelle mir nun im HTML-Format 5 Bullet Points. Jetzt folgen die Daten: """
"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 5 - Hauptprompt WorthKnowingShop
    -> Ziel ist es einen guten WorthKnowingShop zu generieren
"""
system_prompt_5 = "Du bist ein erfahrener und erfolgreicher Redakteur im Contentteam von Relaxdays. Relaxdays hat sich auf den Online-Verkauf von Produkten in den Bereichen Haus, Garten und Freizeit spezialisiert. Die Produkte des Unternehmens werden über einen eigenen Webshop sowie über verschiedene Online-Plattformen an Kunden in ganz Europa vertrieben."
user_prompt_5 = """Deine Herausforderung besteht darin, „Worth Knowing “ für einen neuen Artikel basierend auf nachfolgenden, vorliegenden Produktdaten zu erstellen.
Du solltest dich an folgender Schritt-für-Schritt-Anleitung sorgfältig orientieren:
a)             Produktdaten erfassen: '''<h2>Nostalgische Wandgarderobe mit 5 Haken</h2>
<p>Mit dieser Wandhakenleiste schaffen Sie im Handumdrehen Stauraum für leichte Jacken, Schals oder Schlüssel. Gleichzeitig verleihen Sie Ihrem Eingangsbereich einen antiken, geradezu barocken Look. Ebenso ist die Hakenleiste für Geschirrtücher in der Küche geeignet. Durch die stilvoll eingearbeiteten Ornamente wird die Kleiderhakenleiste auch einzeln zum originellen Dekoelement</p>'''
b)     	Erstelle eine Überschrift die das Produkt gut zusammenfasst hierbei sollst du bestenfalls den Einsatzort mit einbinden. Sei dabei sehr schlau.
c)     	Erstelle nun die Liste hierbei musst du die Positiven Eigenschaften und Vorteile für den Kunden betonen.
d)     	Benutze hierbei Formulierungen die positiven Eigenschaften oder die Vorteile für den Kunden hervorstellen
e)     	Binde jetzt positive Emotionen oder positive Wirkung des Produktes mit in die Formulierungen ein.
f)     	Achte auch darauf, dass du die relevanten Schlüsselwörter miteinfügst.
g)     	Wenn du es kannst, dann benutze Bildliche Formulierungen.
Du sollst nur die Worth Knowing generieren, also auf zusätzliche Umschreibungen, Stichpunkte, Erläuterungen usw. verzichten. Die Worth Knowing Argumente müssen, wie in nachfolgenden Beispielen illustriert, immer eine Überschrift und mindestens fünf Argumente sein, mit HTML-Tags genauso markiert werden, und sollten sehr gut sein.
Jetzt folgen die Daten: """

"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 6 - Hauptprompt MetaKeywordShop
    -> Ziel ist es einen guten MetaKeywordShop zu generieren
"""
system_prompt_6 = "Du bist ein erfahrener und erfolgreicher Redakteur im Contentteam von Relaxdays. Relaxdays hat sich auf den Online-Verkauf von Produkten in den Bereichen Haus, Garten und Freizeit spezialisiert. Die Produkte des Unternehmens werden über einen eigenen Webshop sowie über verschiedene Online-Plattformen an Kunden in ganz Europa vertrieben."
user_prompt_6 = "Generiere einen MetaKeywordShop. Jetzt folgen die Daten: "
"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 7 - Hauptprompt Reprompt
    -> Ziel ist es einen guten Reprompt zu generieren
    -> Es gibt das 
"""
system_prompt_7 = "Du bist ein erfahrener und erfolgreicher Redakteur im Contentteam von Relaxdays. Relaxdays hat sich auf den Online-Verkauf von Produkten in den Bereichen Haus, Garten und Freizeit spezialisiert. Die Produkte des Unternehmens werden über einen eigenen Webshop sowie über verschiedene Online-Plattformen an Kunden in ganz Europa vertrieben."
user_prompt_7 = "Verfeinere das Ergebnis. Jetzt folgen die Daten: "
"""
#########################################################################################################################################################################################################################
"""

hauptprompts = {"system_TitleAmazon" : system_prompt_1,
                "user_TitleAmazon" : user_prompt_1,
                "system_DescriptionLongShops": system_prompt_2,
                "user_DescriptionLongShops": user_prompt_2,
                "system_SalesArgument" : system_prompt_3,
                "user_SalesArgument" : user_prompt_3,
                "system_AmazonBulletPoints" : system_prompt_4,
                "user_AmazonBulletPoints" : user_prompt_4,
                "system_WorthKnowingShop" : system_prompt_5,
                "user_WorthKnowingShop" : user_prompt_5,
                "system_MetaKeywordShop" : system_prompt_6,
                "user_MetaKeywordShop" : user_prompt_6,
                "system_reprompt" : system_prompt_7,
                "user_reprompt" : user_prompt_7
                }