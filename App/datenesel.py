import csv
import openai
import logging
import routes
import prompts
from config import api_key, model, temperature, max_length, top_p, frequency_penalty, presence_penalty

# Konfiguration für den OpenAI GPT-3.5 Aufruf in config
openai.api_key = api_key


def generate_product_features(user_input):

    input = user_input['TitlePlain'] + "// Lieferumfang: " + " / ".join(user_input["DeliveryContents"]) + " // " + " / ".join(user_input["UserInstructions"]) + " // "

    system_prompt = prompts.system_prompt_1
    user_prompt = prompts.user_prompt_1_part1 + input + prompts.user_prompt_1_part2

    routes.status_global = "Prerequests started"

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
        routes.status_global = "Prerequests (" + str(i) + "/4)"

    output = " / ".join(combined_outputs)



    logging.info('Datenesel I: ' + output)

    return output

def refine_product_features(combined_outputs):
    system_prompt = prompts.system_prompt_2
    user_prompt = prompts.user_prompt_2_part1 + combined_outputs + prompts.user_prompt_2_part2

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature,
        max_tokens=max_length,
        top_p=0.5,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    logging.info('Datenesel II (Finished): ' + response.choices[0].message['content'])
    routes.status_global = "Prerequests (4/4)"

    return response.choices[0].message['content']

