import csv
import json
import logging
import openai
import routes
import prompts
from config import api_key, model, temperature, max_length, top_p, frequency_penalty, presence_penalty
from get_embedding import embedding
# Konfiguration für den OpenAI GPT-3.5 Aufruf in config
openai.api_key = api_key


def openai_requests(datenesel, config):

    temperature = config["llm_settings"]["temperature"]
    max_tokens = config["llm_settings"]["max_tokens"]
    top_p = config["llm_settings"]["top_p"]
    frequency_penalty = config["llm_settings"]["frequency_penalty"]
    presence_penalty = config["llm_settings"]["presence_penalty"]

    outputs = []
    #set settings for Openai API calls

    for key in config["generate_selection"].keys():

        if (config["generate_selection"][key] == True):
            routes.status_global["Hauptabfrage " + key] = True  # status update

            system_prompt = prompts.hauptprompts["system_" + key]
            user_prompt = prompts.hauptprompts["user_" + key] + datenesel

            if key != 'MetaKeywordShop':
                user_prompt += embedding(datenesel, key)


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

            logging.info('Hauptabfrage ' + key + ': ' + response.choices[0].message['content'])

            outputs.append({"typ" : key,
                            "prompt" : user_prompt,
                            "response" : response.choices[0].message['content']
                        })
            routes.status_global["Antwort " + key] = True        # status update

        else:
            routes.status_global["Hauptabfrage " + key] = False  # status update
            routes.status_global["Antwort " + key] = False
            logging.info('Hauptabfrage ' + key + ': not selected')

    return json.dumps(outputs)

