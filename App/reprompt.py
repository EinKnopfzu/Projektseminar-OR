import csv
import pandas as pd
import random
import json
import logging
import openai
import routes
import prompts
from  check_structures import check_html, check_length
from config import api_key, model, temperature, max_length, top_p, frequency_penalty, presence_penalty
# Konfiguration für den OpenAI GPT-3.5 Aufruf in config
openai.api_key = api_key


def reprompt_request(config):
    routes.status_global["Hauptabfrage Reprompt"] = False
    routes.status_global["Antwort Reprompt"] = False        # status update

    temperature = config["llm_settings"]["temperature"]
    max_tokens = config["llm_settings"]["max_tokens"]
    top_p = config["llm_settings"]["top_p"]
    frequency_penalty = config["llm_settings"]["frequency_penalty"]
    presence_penalty = config["llm_settings"]["presence_penalty"]

    if config["llm_settings"]["select_llm"] == "Llama-selbstrainiert":
        logging.info('LLAMA ist noch nicht angebunden')
        exit(0)

     # status update

    system_prompt = prompts.hauptprompts["system_reprompt"]

    routes.status_global["Hauptabfrage Reprompt"] = True                    # status update

    # random_dialogue = pd.read_csv("preprocessed_embeddings.csv").sample(n=1).iloc[0]
    
    if config["typ"] in ('DescriptionLongShops'):
        for i in range(5):
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    # {"role": "user", "content": random_dialogue['Inputdata']},
                    # {"role": "assistant", "content": random_dialogue[config["typ"]]},                    
                    {"role": "user", "content": config["prompt_original"]},
                    {"role": "assistant", "content": config["prompt_response"]},
                    {"role": "user", "content": config["instruction"] + "\n" + prompts.hauptprompts["struct_" + config["typ"]]},
                    {"role": "user", "content": config["prompt_original"]}
                ],
                temperature=0.5,
                max_tokens=max_length,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty
            )
            response_try = response.choices[0].message['content']
            if (check_html(config["typ"], response_try) == True):
                break
    else:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": config["prompt_original"]},
                {"role": "assistant", "content": config["prompt_response"]},
                {"role": "user", "content": config["instruction"]}
            ],
            temperature=0.5,
            max_tokens=max_length,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )        
        

    logging.info('Hauptabfrage Reprompt: ' + response.choices[0].message['content'])

    routes.status_global["Antwort Reprompt"] = True  # status update

    return json.dumps({"typ": config["typ"],
                    "prompt": config["instruction"],
                    "response": response.choices[0].message['content']
                    })

