import openai
import requests

openai.api_key = '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'

def dalle(msg_arr):
    user_keyword = ""
    for keyword in msg_arr:
        user_keyword+=keyword

    # 시스템 임의 설정
    add_prompt = "background"
    input_prompt=user_keyword+add_prompt

    response = openai.Image.create(
        prompt=input_prompt,
        n=3,
        size="512x512",
        response_format="url"
    )
    image_url1 = response['data'][0]['url']
    image_url2 = response['data'][1]['url']
    image_url3 = response['data'][2]['url']

    return image_url1, image_url2, image_url3