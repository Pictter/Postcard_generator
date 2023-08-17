import openai
import requests

openai.api_key = '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'

def dalle(msg_arr):
    user_keyword = ""
    for keyword in msg_arr:
        user_keyword+=keyword

    # 시스템 임의 설정
    add_prompt = "background, no text"
    input_prompt=user_keyword+add_prompt

    response = openai.Image.create(
        prompt=input_prompt,
        n=3,
        size="512x512",
        response_format="url"
    )
    # image_url3 = response['data'][2]['url']

    return response