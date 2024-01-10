import csv
import json
import logging
import openai
import routes
from config import api_key, model, temperature, max_length, top_p, frequency_penalty, presence_penalty
# Konfiguration für den OpenAI GPT-3.5 Aufruf in config
openai.api_key = api_key


def openai_requests(datenesel, config):

    routes.status_global = "Mainrequests started"
    outputs = []

    if (config['Title?'] == 1):

        system_prompt = "Generiere einen Titel"
        user_prompt = "Generiere einen Titel mit den Daten " + datenesel

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

        logging.info('Final Request Title: ' + response.choices[0].message['content'])

        outputs.append(['Title?', response.choices[0].message['content']])

    if (config['DescriptionLong?'] == 1):
        system_prompt = "Generiere eine Produktbeschreibung"
        user_prompt = "Generiere eine Produktbeschreibung mit den Daten " + datenesel

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

        logging.info('Final Request DescriptionLong: ' + response.choices[0].message['content'])

        outputs.append(['DescriptionLong?', response.choices[0].message['content']])

    if (config['SalesArguments?'] == 1):
        system_prompt = "Generiere SalesArguments"
        user_prompt = "Generiere SalesArguments mit den Daten " + datenesel

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

        logging.info('Final Request SalesArguments: ' + response.choices[0].message['content'])

        outputs.append(['SalesArguments?', response.choices[0].message['content']])

    if (config['BulletPoints?'] == 1):
        system_prompt = "Generiere BulletPoints"
        user_prompt = "Generiere BulletPoints mit den Daten " + datenesel

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

        logging.info('Final Request BulletPoints: ' + response.choices[0].message['content'])

        outputs.append(['BulletPoints?', response.choices[0].message['content']])

    if (config['xxx?'] == 1):
        system_prompt = "Generiere xxx"
        user_prompt = "Generiere xxx mit den Daten " + datenesel

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

        logging.info('Final Request xxx: ' + response.choices[0].message['content'])


        outputs.append(['xxx', response.choices[0].message['content']])

    logging.info('Final Request all_combined: ' + str(outputs))

    routes.status_global = "Mainrequests finished"

    return json.dumps(outputs)