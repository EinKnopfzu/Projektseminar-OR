import csv
import openai
import tiktoken # kann wahrscheinlich weg (nur für Berechnung der Kosten)
import numpy as np

openai.api_key = 'YOLO'

def cosine_similarity(vec_a, vec_b):
    return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))

def get_embedding(text):
    text = text.replace("\n", " ").strip()
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

# Mit dem eigentlichen Datenesel ersetzen (aktuell Dummy)
predefined_text = "DescriptionLongMarketplaces für // Elektrischer Milchaufschäumer // Lieferumfang: 1x Milchaufschäumer, 1x Basisstation // Milchaufschäumer im Überblick: Abmessungen H x B x T: ca. 20 x 10 x 10 cm / Fassungsvermögen: 250 ml / Leistung: 500W / Material: Edelstahl, Kunststoff / Farbe: Silber oder Schwarz // Stilvolles Design in Silber oder Schwarz / Vielseitig einsetzbar für die Zubereitung von verschiedenen Milchgetränken / Großzügiges Fassungsvermögen für die Zubereitung mehrerer Portionen / Hochleistungsstarker Motor für schnelles und effizientes Aufschäumen / Hochwertige Materialkombination aus Edelstahl und Kunststoff für langlebige Nutzung / Praktische Basisstation für bequeme Aufbewahrung und kabelloses Aufwärmen / Einfache Reinigung und Pflege des Milchaufschäumers / Leistungsstarke 500W für schnelle Aufschäumung / Vielseitige Anwendungsmöglichkeiten für die Zubereitung von verschiedenen Kaffeespezialitäten / Modernes und ansprechendes Design für die Küchendekoration"

predefined_embedding = get_embedding(predefined_text)

# kann wahrscheinlich weg (nur für Berechnung der Kosten)
def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def main():
    input_file_path = 'DatenDescriptionLongShops1-616.csv'
        
    with open(input_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    similarities = []
    total_cost = 0 # kann wahrscheinlich weg (nur für Berechnung der Kosten)
    
    for row in rows:
        text = row['User'].replace('DescriptionLongShops für // ', '')
        embedding = get_embedding(text)
        row['Embedding'] = embedding

        num_tokens = num_tokens_from_string(text) # kann wahrscheinlich weg (nur für Berechnung der Kosten)
        price_per_token = 0.0000001 # kann wahrscheinlich weg (nur für Berechnung der Kosten)
        cost = num_tokens * price_per_token # kann wahrscheinlich weg (nur für Berechnung der Kosten)
        total_cost += cost # kann wahrscheinlich weg (nur für Berechnung der Kosten)
        
        similarity = cosine_similarity(embedding, predefined_embedding)
        text_start = text.split(" //")[0] if " //" in text else text
        similarities.append((text_start, similarity))
        print(f"Text: {text}\nÄhnlichkeit mit vordefiniertem Text: {similarity}\nAnzahl der Tokens: {num_tokens}\nKosten für diesen Aufruf: ${cost:.8f}\n")

    with open(input_file_path, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = reader.fieldnames + ['Embedding']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

    similarities.sort(key=lambda x: x[1], reverse=True)

    print(f"Gesamtkosten für alle Abfragen insg.: ${total_cost:.8f}")

    print("Top 10 der höchsten Ähnlichkeiten:")
    for i, (text, similarity) in enumerate(similarities[:10], start=1):
        print(f"{i}.) {text}, {similarity:.8f}")

if __name__ == '__main__':
    main()
