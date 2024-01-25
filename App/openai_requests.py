import csv
import pandas as pd
import json
import logging
import openai
import routes
import prompts
from config import api_key, model, temperature, max_length, top_p, frequency_penalty, presence_penalty
from get_embedding import embedding
from check_structures import check_structure
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

            if key not in ('SalesArgument', 'WorthKnowingShop', 'DescriptionLongShops'):
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
            else:
                system_prompt = prompts.hauptprompts["system_" + key]
                user_prompt = datenesel
                dialogue = embedding(datenesel, key)
                for i in range(3):
                    response = openai.ChatCompletion.create(
                        model=model,
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": dialogue.iloc[0]['Inputdata']},                        
                            {"role": "assistant", "content": dialogue.iloc[0][key]},
                            {"role": "user", "content": dialogue.iloc[1]['Inputdata']},       
                            {"role": "assistant", "content": dialogue.iloc[1][key]},
                            {"role": "user", "content": dialogue.iloc[2]['Inputdata']},       
                            {"role": "assistant", "content": dialogue.iloc[2][key]},
                            {"role": "user", "content": user_prompt}      
                        ],
                        temperature=temperature,
                        max_tokens=max_length,
                        top_p=top_p,
                        frequency_penalty=frequency_penalty,
                        presence_penalty=presence_penalty
                    )
                    response_try = response.choices[0].message['content']
                    if check_structure(key, response_try):
                        break
            
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

