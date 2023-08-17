import openai
import requests

openai.api_key = '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'

def dalle(msg_arr):
    user_keyword = ""
    for keyword in msg_arr:
        user_keyword+=keyword

    # 시스템 임의 설정
    input_prompt="create background postcard painting with"+user_keyword+"and no person and text."

    response = openai.Image.create(
        prompt=input_prompt,
        n=3,
        size="512x512",
        response_format="url"
    )
    # image_url3 = response['data'][2]['url']

    return response