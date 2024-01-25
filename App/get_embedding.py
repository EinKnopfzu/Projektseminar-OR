import csv
import openai
import numpy as np
import ast
import pandas as pd
from config import api_key
import routes

openai.api_key = api_key
def cosine_similarity(vec_a, vec_b):
    return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a,2) * np.linalg.norm(vec_b,2))

def abfrage(datenesel):
    datenesel = datenesel.replace("\n", " ").strip()
    response = openai.Embedding.create(input=datenesel, model="text-embedding-ada-002")
    return response['data'][0]['embedding']


def embedding(datenesel, typ_key):

    persistant_dataframe_embedding = pd.read_csv("preprocessed_embeddings.csv")
    routes.status_global["Datenähnlichkeiten gestartet"] = True  # status update

    predefined_embedding = abfrage(datenesel)

    similarity = []

    for index, row in persistant_dataframe_embedding.iterrows():
        embedding_list = row["Embedding"][1:][:-1].split(",")

        similarity.append(cosine_similarity(ast.literal_eval(row['Embedding']), predefined_embedding))

    persistant_dataframe_embedding["similarity"] = similarity
    persistant_dataframe_embedding = persistant_dataframe_embedding.sort_values(by=["similarity"], ascending = False)


    result = []
    for index in range(0,3):
        if typ_key == 'AmazonBulletPoints':
            result.append("<ul><li>" + persistant_dataframe_embedding["AmazonBulletPoint1"][index] + "</li><li>" + persistant_dataframe_embedding["AmazonBulletPoint2"][index] + "</li><li>" + persistant_dataframe_embedding["AmazonBulletPoint3"][index] + "</li><li>" + persistant_dataframe_embedding["AmazonBulletPoint4"][index] + "</li><li>" + persistant_dataframe_embedding["AmazonBulletPoint5"][index] + "</li></ul>")
        elif typ_key == 'SalesArgument':
            return persistant_dataframe_embedding[['Inputdata', typ_key]].head(3)
        else:
            result.append(persistant_dataframe_embedding[typ_key][index])

    routes.status_global["Datenähnlichkeiten abgeschlossen"] = True  # status update

    return '\n'.join(result)

