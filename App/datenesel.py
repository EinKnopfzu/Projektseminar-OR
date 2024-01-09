import csv
import openai

# Konfiguration für den OpenAI GPT-3.5 Aufruf
openai.api_key = 'sk-WaW2BdK32wLVmLnknjpdT3BlbkFJEwENS02Cp3Vyvt5e4zkyyy'
model = 'gpt-3.5-turbo-1106'
temperature = 1
max_length = 2048
top_p = 1
frequency_penalty = 0
presence_penalty = 0

def generate_product_features(user_input):

    line = user_input['TitlePlain'] + "// Lieferumfang: " + " / ".join(user_input["DeliveryContents"]) + " // " + " / ".join(user_input["UserInstructions"]) + " // "

    system_prompt = "Du bist ein Spezialist für E-Commerce und SEO. Du hast Expertise im Extrahieren und Abstrahieren von Produktmerkmalen, welche entscheidend für die Kaufentscheidung sind, welche helfen, die Vorzüge eines Produktes zu erkennen, und welche die Benutzererfahrung hervorheben. Du arbeitest marketing- und zielgruppenorientiert. Du antwortest immer in folgendem Format: 'Produktmerkmal 1 / Produktmerkmal 2 / [...] / Produktmerkmal x'."
    user_prompt = f"Extrahiere und abstrahiere ca. 10 Produktmerkmale anhand der folgenden Produktdaten:\n\n'{line}'\n\nIdentifiziere attraktive, verkaufsfördernde Merkmale, die für diese Produktart typisch sind, ohne jedoch spezifische Funktionen oder Eigenschaften zu erfinden, die nicht im Datensatz erwähnt werden. Stelle sicher, dass die Merkmale zwar einer subjektiven, positiven Beurteilung ähneln, aber realistisch und in Übereinstimmung mit den gegebenen Produktdaten sind. Vermeide übertriebene Annahmen oder Ergänzungen, die kaum aus den gegebenen Informationen abgeleitet werden können.\n\nAntworte im Format 'Produktmerkmal 1 / Produktmerkmal 2 / ... / Produktmerkmal x'."
    
    combined_outputs = []
    for _ in range(3):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature,
            max_tokens=max_length,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )
        combined_outputs.append(response.choices[0].message['content'])
    
    return " / ".join(combined_outputs)

def refine_product_features(combined_outputs):
    system_prompt = "Du bist ein Spezialist für E-Commerce und SEO. Du hast Expertise im Extrahieren und Abstrahieren von Produktmerkmalen, welche entscheidend für die Kaufentscheidung sind, welche helfen, die Vorzüge eines Produktes zu erkennen, und welche die Benutzererfahrung hervorheben. Du arbeitest marketing- und zielgruppenorientiert. Du antwortest immer in folgendem Format: 'Produktmerkmal 1 / Produktmerkmal 2 / [...] / Produktmerkmal x'."
    user_prompt = f"Extrahiere ca. 10 Produktmerkmale aus den folgenden Produktmerkmalen:\n\n'{combined_outputs}'\n\nIdentifiziere attraktive, verkaufsfördernde Merkmale, die für diese Produktart typisch sind. Stelle sicher, dass die Merkmale einer subjektiven, positiven Beurteilung ähneln, wie z.B. 'stilvolles Design', 'hoher Komfort' oder 'benutzerfreundliche Handhabung'. Entferne bzw. ignoriere Merkmale, die objektiverer Natur sind und sich oft in Zahlen ausdrücken, wie z.B. '3m breit' oder '40 Stück in rot und blau'. Unerwünschte Merkmale sind hier oft solche, die sich auf einem Produktdatenblatt wiederfinden würden. Du kannst objektive, spezifische Produktdetails durch beschreibende Adjektive ersetzen, die die Qualität, Funktionalität oder das Erscheinungsbild des Produkts beschreiben, wie z.B. 'leicht', 'robust' oder 'elegant'. Berücksichtige die Zielgruppe und den vorgesehenen Verwendungszweck des Produkts bei der Auswahl der Merkmale, wenn deutlich wird, um was für ein Produkt es sich handelt. Wähle Merkmale, die für potenzielle Käufer am ansprechendsten und relevantesten sind. Vermeide sehr übertriebene Aussagen.\n\nAntworte im Format 'Produktmerkmal 1 / Produktmerkmal 2 / ... / Produktmerkmal x'."

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature,
        max_tokens=max_length,
        top_p=0.5,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    return response.choices[0].message['content']

