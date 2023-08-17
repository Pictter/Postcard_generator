import openai
import requests
import dotenv
import os

# OpenAI API 키 설정
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
openai.api_key = os.environ["API_KEY"]

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
    
    image_url3 = response['data'][2]['url']

    return response