import csv
import pandas as pd
import random
import json
import logging
import openai
import routes
import prompts
from  check_structures import check_html, check_length, check_lies
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
    if config["prompt_original"].count("\n\n## USER:\n") == 4:
        original_prompt = config["prompt_original"].split("\n\n## USER:\n")[4].split("\n\n## ASSISTANT:")[0]
    else:
        original_prompt = config["prompt_original"].split("\n\n## USER:\n")[1].split("1.) Produktdaten:\n")[1].split("\n\n2.) Originaltext:\n")[0]
    original_response = config["prompt_response"]
    if config["prompt_original"].count("\n\n## USER:\n") == 4:
        instruction = config["instruction"]
    else:
        instruction = config["prompt_original"].split("\n\n3.) Anweisung(en) zur Anpassung des Originaltextes:\n")[1].split("\n\n")[0]
        instruction += "\n" + config["instruction"]
    structure = prompts.hauptprompts["struct_" + config["typ"]]
    new_prompt = "1.) Produktdaten:\n" + original_prompt + "\n\n2.) Originaltext:\n" + original_response + "\n\n3.) Anweisung(en) zur Anpassung des Originaltextes:\n" + instruction + "\n\n" + structure

    routes.status_global["Hauptabfrage Reprompt"] = True                    # status update


    
    if config["typ"] in ('SalesArgument', 'WorthKnowingShop', 'DescriptionLongShops', 'AmazonBulletPoints', 'MetaKeywordShop'):
        for i in range(5):
            response = openai.ChatCompletion.create(
                model='gpt-4-0125-preview',
                messages=[
                    {"role": "system", "content": system_prompt},             
                    {"role": "user", "content": new_prompt}
                ],
                temperature=temperature,
                max_tokens=max_length,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty
            )
            response_try = response.choices[0].message['content']
            if check_html(config["typ"], response_try) and check_length(config["typ"], response_try, i):
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
                    "prompt": "## SYSTEM:\n" + system_prompt + "\n\n##################################################################################################" +
                               "\n\n## USER:\n" + new_prompt + "\n\n## ASSISTANT:\n",
                    "response": response.choices[0].message['content']
                    })

