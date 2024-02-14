import csv
import openai
import logging
import routes
import prompts
import random
from check_structures import check_lies
from config import api_key, model, temperature, max_length, top_p, frequency_penalty, presence_penalty

# Konfiguration für den OpenAI GPT-3.5 Aufruf in config
openai.api_key = api_key


def generate_product_features(user_input):

    temperature = 1
    max_tokens = 4095
    top_p = 1
    frequency_penalty = 0
    presence_penalty = 0

    if user_input["llm_settings"]["select_llm"] == "Llama-selbstrainiert":
        logging.info('LLAMA ist noch nicht angebunden')                 #Killswitch nicht implemented yet
        exit(0)

    input = user_input["product_information"]["TitlePlain"] + " // Lieferumfang: " + " / ".join(user_input["product_information"]["DeliveryContents"]) + " // " + " / ".join(user_input["product_information"]["UserInstructions"]) + " // "

    routes.status_global["Daten vorverarbeitet"] = True                 # status update


    system_prompt = prompts.pre_system_prompt_1
    user_prompt = prompts.pre_user_prompt_1_part1 + input + prompts.pre_user_prompt_1_part2

    combined_outputs = []
    for i in range(3):
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
        combined_outputs.append(response.choices[0].message['content'])
        
    random.shuffle(combined_outputs)
    output = " / ".join(combined_outputs)

    routes.status_global["Daten vorabgefragt"] = True                       # status update

    logging.info('Datenesel vorabgefragt: ' + output)

    return {"output" : output, "input" : input}

def refine_product_features(combined_outputs, input):
    system_prompt = prompts.pre_system_prompt_2
    user_prompt = prompts.pre_user_prompt_2_part1 + combined_outputs + prompts.pre_user_prompt_2_part2 + input + prompts.pre_user_prompt_2_part3
    for i in range(3):
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
        if check_lies(input, response.choices[0].message['content']) and response.choices[0].message['content'].count("/") >= 9:
            break
            
    logging.info('Datenesel erstellt: ' + input + response.choices[0].message['content'])

    routes.status_global["Datenesel erstellt"] = True                          # status update

    return input + response.choices[0].message['content']

