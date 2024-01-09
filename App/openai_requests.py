import csv
import json

import openai

# Konfiguration für den OpenAI GPT-3.5 Aufruf
openai.api_key = 'sk-WaW2BdK32wLVmLnknjpdT3BlbkFJEwENS02Cp3Vyvt5e4zkyyy'
model = 'gpt-3.5-turbo-1106'
temperature = 1
max_length = 2048
top_p = 1
frequency_penalty = 0
presence_penalty = 0

def openai_requests(datenesel, config):

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

        outputs.append(['xxx', response.choices[0].message['content']])

    return json.dumps(outputs)
