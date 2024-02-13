import prompts
import openai



def check_length(key, response_text, i):
    if key == 'DescriptionLongShops':
        if i == 0:
            return 400 <= (len(response_text) - len("<h2>") - len("</h2><p>") - len("</p>")) <= 550
        elif i == 1:
            return 300 <= (len(response_text) - len("<h2>") - len("</h2><p>") - len("</p>")) <= 650
        else:
            return True
    if key == 'TitleAmazon':
        if i == 0:
            return 40 <= len(response_text) <= 100
        elif i == 1:
            return 40 <= len(response_text) <= 120
        else:
            return True
    else:
        return True



def check_html(key, response_text):
    if key == 'SalesArgument':
        return (response_text.startswith(("<ul><li>", "<ul>\n<li>"))
            and (response_text.count("</li><li>") + response_text.count("</li>\n<li>") == 4)
            and response_text.endswith(("</li></ul>", "</li>\n</ul>")))
    if key == 'WorthKnowingShop':
        return (response_text.startswith("<h2>")
            and ("</h2><ul><li>" in response_text)
            and (response_text.count("</li><li>") == 5)
            and (response_text.endswith("</li></ul>")))
    if key == 'DescriptionLongShops':
        return ((response_text.startswith("<h2>"))
            and ("</h2><p>" in response_text)
            and (response_text.endswith("</p>")))
    if key == 'TitleAmazon':
        return response_text.startswith("Relaxdays ")
    else:
        return True



def check_lies(input, response_text):
    system_prompt = prompts.pre_system_prompt_3
    user_prompt = prompts.pre_user_prompt_3_part1 + input + prompts.pre_user_prompt_3_part2 + response_text + prompts.pre_user_prompt_3_part3
    response = openai.ChatCompletion.create(
        model='gpt-4-0125-preview',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=4095,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if response.choices[0].message['content'].endswith("nein"):
        return True
    else:
        return False



def check_AmazonBulletPoints(bullet_text):
    return bullet_text[7:-3]
