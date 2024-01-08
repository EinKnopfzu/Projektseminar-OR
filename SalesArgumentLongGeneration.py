import csv
import openai

# Konfiguration für den OpenAI GPT-3.5 Aufruf
openai.api_key = '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'
model = 'gpt-3.5-turbo-1106'
temperature = 1
max_length = 2048
top_p = 1
frequency_penalty = 0
presence_penalty = 0

def generate_product_features(line):
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
        output = response.choices[0].message['content']
        print(f"Generierte Variante: {output}\n")  # Ausgabe der generierten Variante
        combined_outputs.append(output)
    
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
    refined_output = response.choices[0].message['content']
    print(f"Verfeinerter Output: {refined_output}\n\n- - - - - -\n")  # Ausgabe des verfeinerten Outputs
    return refined_output

def main():
    input_file_path = 'InputDaten31-60.csv'
    output_file_path = 'ErweiterteDaten31-60-3.5-turbo.csv'

    with open(input_file_path, mode='r', encoding='utf-8') as infile, \
         open(output_file_path, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if row[0].startswith('DescriptionLongMarketplaces für // '):
                original_line = row[0].replace('DescriptionLongMarketplaces für // ', '')
                try:
                    combined_outputs = generate_product_features(original_line)
                    refined_output = refine_product_features(combined_outputs)
                    new_line = row[0] + refined_output
                    writer.writerow([new_line])
                except Exception as e:
                    print(f"Error processing line: {row[0]}, Error: {e}")
            else:
                writer.writerow(row)

if __name__ == '__main__':
    main()
