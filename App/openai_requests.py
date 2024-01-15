import csv
import json
import logging
import openai
import routes
import prompts
from config import api_key, model, temperature, max_length, top_p, frequency_penalty, presence_penalty
# Konfiguration für den OpenAI GPT-3.5 Aufruf in config
openai.api_key = api_key


def openai_requests(datenesel, config):

    max_operations = get_count(config)
    counter = 0
    outputs = []

    counter = set_counter(counter, max_operations)

    if (config['Title?'] == 1):

        system_prompt = prompts.system_prompt_3
        user_prompt = prompts.user_prompt_3 + datenesel

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
        counter = set_counter(counter, max_operations)

    if (config['DescriptionLong?'] == 1):
        system_prompt = prompts.system_prompt_4
        user_prompt = prompts.user_prompt_4 + datenesel

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
        counter = set_counter(counter, max_operations)

    if (config['SalesArguments?'] == 1):
        system_prompt = prompts.system_prompt_5
        user_prompt = prompts.user_prompt_5 + datenesel

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
        counter = set_counter(counter, max_operations)

    if (config['BulletPoints?'] == 1):
        system_prompt = prompts.system_prompt_6
        user_prompt = prompts.user_prompt_6 + datenesel

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
        counter = set_counter(counter, max_operations)


    if (config['xxx?'] == 1):
        system_prompt = prompts.system_prompt_7
        user_prompt = prompts.user_prompt_7 + datenesel

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
        counter = set_counter(counter, max_operations)

    logging.info('Final Request all_combined: ' + str(outputs))

    routes.status_global = "Mainrequests finished"

    return json.dumps(outputs)


def get_count(config):
    count_operations = 0

    if config['Title?'] == 1:
        count_operations += 1

    if config['DescriptionLong?'] == 1:
        count_operations += 1

    if config['SalesArguments?'] == 1:
        count_operations += 1

    if config['BulletPoints?'] == 1:
        count_operations += 1

    if config['xxx?'] == 1:
        count_operations += 1

    return count_operations

def set_counter(counter, max_operations):
    routes.status_global = "Mainrequests (" + str(counter) + "/" + str(max_operations) + ")"
    return counter + 1