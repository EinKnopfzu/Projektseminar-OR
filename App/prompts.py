"""
In diesem File werden die Prompts bzw. Prompt Teile für die Abfragen verwaltet!
#######################################################################################################################################################################################################
"""
"""
Prompt 1 - Generate Product Features
    -> Vorabfrage um einen Datenesel aufzubauen
    -> wird 3x ausgeführt
"""
system_prompt_1 = "Du bist ein Spezialist für E-Commerce und SEO. Du hast Expertise im Extrahieren und Abstrahieren von Produktmerkmalen, welche entscheidend für die Kaufentscheidung sind, welche helfen, die Vorzüge eines Produktes zu erkennen, und welche die Benutzererfahrung hervorheben. Du arbeitest marketing- und zielgruppenorientiert. Du antwortest immer in folgendem Format: 'Produktmerkmal 1 / Produktmerkmal 2 / [...] / Produktmerkmal x'."
user_prompt_1_part1 = "Extrahiere und abstrahiere ca. 10 Produktmerkmale anhand der folgenden Produktdaten:\n\n"
user_prompt_1_part2 = "\n\nIdentifiziere attraktive, verkaufsfördernde Merkmale, die für diese Produktart typisch sind, ohne jedoch spezifische Funktionen oder Eigenschaften zu erfinden, die nicht im Datensatz erwähnt werden. Stelle sicher, dass die Merkmale zwar einer subjektiven, positiven Beurteilung ähneln, aber realistisch und in Übereinstimmung mit den gegebenen Produktdaten sind. Vermeide übertriebene Annahmen oder Ergänzungen, die kaum aus den gegebenen Informationen abgeleitet werden können.\n\nAntworte im Format 'Produktmerkmal 1 / Produktmerkmal 2 / ... / Produktmerkmal x'."

"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 2 - Refine Product Features
    -> Vorabfrage um einen Datenesel aufzubauen
    -> wird 1x ausgeführt und kombiniert die 3 erzeugten Prompt zu einem
"""
system_prompt_2 = "Du bist ein Spezialist für E-Commerce und SEO. Du hast Expertise im Extrahieren und Abstrahieren von Produktmerkmalen, welche entscheidend für die Kaufentscheidung sind, welche helfen, die Vorzüge eines Produktes zu erkennen, und welche die Benutzererfahrung hervorheben. Du arbeitest marketing- und zielgruppenorientiert. Du antwortest immer in folgendem Format: 'Produktmerkmal 1 / Produktmerkmal 2 / [...] / Produktmerkmal x'."
user_prompt_2_part1 = "Extrahiere ca. 10 Produktmerkmale aus den folgenden Produktmerkmalen:\n\n"
user_prompt_2_part2 = "\n\nIdentifiziere attraktive, verkaufsfördernde Merkmale, die für diese Produktart typisch sind. Stelle sicher, dass die Merkmale einer subjektiven, positiven Beurteilung ähneln, wie z.B. 'stilvolles Design', 'hoher Komfort' oder 'benutzerfreundliche Handhabung'. Entferne bzw. ignoriere Merkmale, die objektiverer Natur sind und sich oft in Zahlen ausdrücken, wie z.B. '3m breit' oder '40 Stück in rot und blau'. Unerwünschte Merkmale sind hier oft solche, die sich auf einem Produktdatenblatt wiederfinden würden. Du kannst objektive, spezifische Produktdetails durch beschreibende Adjektive ersetzen, die die Qualität, Funktionalität oder das Erscheinungsbild des Produkts beschreiben, wie z.B. 'leicht', 'robust' oder 'elegant'. Berücksichtige die Zielgruppe und den vorgesehenen Verwendungszweck des Produkts bei der Auswahl der Merkmale, wenn deutlich wird, um was für ein Produkt es sich handelt. Wähle Merkmale, die für potenzielle Käufer am ansprechendsten und relevantesten sind. Vermeide sehr übertriebene Aussagen.\n\nAntworte im Format 'Produktmerkmal 1 / Produktmerkmal 2 / ... / Produktmerkmal x'."


"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 3 - Hauptprompt Titel
    -> Ziel ist es einen guten Titel zu generieren
"""
system_prompt_3 = "Generiere einen Titel"
user_prompt_3 = "Generiere einen Titel mit den Daten "

"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 4 - Hauptprompt DescriptionLong
    -> Ziel ist es einen guten DescriptionLong zu generieren
"""
system_prompt_4 = "Generiere einen Produktbeschreibung"
user_prompt_4 = "Generiere einen Produktbeschreibung mit den Daten "

"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 5 - Hauptprompt SalesArguments
    -> Ziel ist es einen guten SalesArguments zu generieren
"""
system_prompt_5 = "Generiere einen SalesArguments"
user_prompt_5 = "Generiere einen SalesArguments mit den Daten "
"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 6 - Hauptprompt BulletPoints
    -> Ziel ist es einen guten BulletPoints zu generieren
"""
system_prompt_6 = "Generiere einen BulletPoints"
user_prompt_6 = "Generiere einen BulletPoints mit den Daten "
"""
#########################################################################################################################################################################################################################
"""

"""
Prompt 7 - Hauptprompt xxx
    -> Ziel ist es einen guten xxx zu generieren
"""
system_prompt_7 = "Generiere einen xxx"
user_prompt_7 = "Generiere einen xxx mit den Daten "