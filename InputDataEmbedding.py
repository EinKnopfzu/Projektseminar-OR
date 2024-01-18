import csv
import openai
import numpy as np

openai.api_key = 'YOLO'

def cosine_similarity(vec_a, vec_b):
    return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))

def get_embedding(text):
    text = text.replace("\n", " ").strip()
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

# Mit dem eigentlichen Datenesel ersetzen (aktuell Dummy)
predefined_text = "'Urban Explorer' Fahrradtasche // Lieferumfang: 1x Fahrradtasche mit Schultergurt // Fahrradtasche im Fokus: Maße H x B x T: ca. 30 x 40 x 10 cm / Volumen: ca. 12 Liter / Gewicht: ca. 800 g / Material: wasserabweisendes Polyester / Farbe: Grau oder Grün // ""Wasserabweisendes Polyester für Schutz vor Regen und Feuchtigkeit / Geräumiges Volumen von 12 Litern für ausreichend Stauraum / Leichtes Gewicht von nur 800 g für angenehmes Tragen / Vielseitige Farbauswahl in Grau oder Grün für individuellen Stil / Praktische Maße von ca. 30 x 40 x 10 cm passend für diverse Fahrradtypen / Inklusive Schultergurt für bequemen Transport außerhalb des Fahrrads / Robuste Materialqualität für langlebige Nutzung / Fokus auf urbanes Design für den modernen Radfahrer / Einfach zu reinigen für pflegeleichte Handhabung / Hochwertige Verarbeitung für strapazierfähige Begleitung"

predefined_embedding = get_embedding(predefined_text)

def main():
    input_file_path = 'DatenDescriptionLongShops1-616.csv'
        
    with open(input_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    similarities = []
    
    for row in rows:
        text = row['User'].replace('DescriptionLongShops für // ', '')

        embedding_array = np.fromstring(row['Embedding'].strip("[]"), sep=', ')
        
        similarity = cosine_similarity(embedding_array, predefined_embedding)
        text_start = text.split(" //")[0] if " //" in text else text
        similarities.append((text_start, similarity))
        print(f"Text: {text}\nÄhnlichkeit mit vordefiniertem Text: {similarity}\n")

    similarities.sort(key=lambda x: x[1], reverse=True)

    print("Top 10 der höchsten Ähnlichkeiten:")
    for i, (text, similarity) in enumerate(similarities[:10], start=1):
        print(f"{i}.) {text}, {similarity:.8f}")

if __name__ == '__main__':
    main()
