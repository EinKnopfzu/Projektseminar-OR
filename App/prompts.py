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
system_prompt_1 = "Generiere einen AmazonTitle"
user_prompt_1 = "Generiere einen AmazonTitle mit den Daten "

"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 2 - Hauptprompt DescriptionLongShops
    -> Ziel ist es einen guten DescriptionLongShops zu generieren
"""
system_prompt_2 = "Generiere einen DescriptionLongShops"
user_prompt_2 = "Generiere einen DescriptionLongShops mit den Daten "

"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 3 - Hauptprompt SalesArguments
    -> Ziel ist es einen guten SalesArguments zu generieren
"""
system_prompt_3 = "Generiere einen SalesArguments"
user_prompt_3 = "Generiere einen SalesArguments mit den Daten "
"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 4 - Hauptprompt AmazonBulletPoints
    -> Ziel ist es einen guten AmazonBulletPoints zu generieren
"""
system_prompt_4 = "Generiere einen AmazonBulletPoints"
user_prompt_4 = "Generiere einen AmazonBulletPoints mit den Daten "
"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 5 - Hauptprompt WorthKnowingShop
    -> Ziel ist es einen guten WorthKnowingShop zu generieren
"""
system_prompt_5 = "Generiere einen WorthKnowingShop"
user_prompt_5 = "Generiere einen WorthKnowingShop mit den Daten "

"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 6 - Hauptprompt MetaKeywordShop
    -> Ziel ist es einen guten MetaKeywordShop zu generieren
"""
system_prompt_6 = "Generiere einen MetaKeywordShop"
user_prompt_6 = "Generiere einen MetaKeywordShop mit den Daten "
"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 7 - Hauptprompt Reprompt
    -> Ziel ist es einen guten Reprompt zu generieren
    -> Es gibt das 
"""
system_prompt_7 = "Verfeinere das Ergebnis nach den Vorgaben "
user_prompt_7 = "Verfeinere das Ergebnis nach den Vorgaben  "
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