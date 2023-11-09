import openai
import dotenv
import os

# OpenAI API 키 설정
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
openai.api_key = os.environ["API_KEY"]


# ChatGPT API 호출
def ChatGPT(input_msg):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 사용할 엔진 선택
        messages=[
            {
                "role": "system",
                "content": "이 메시지의 분위기를 파악하여 5개의 키워드를 선택하고, 결과를 한국어로 반환하십시오.",
            },
            {
                "role": "system",
                "content": "단어1, 단어2, 단어3, 단어4, 단어5 형태로 반환하십시오.",
            },
            {"role": "user", "content": input_msg},
        ],
        max_tokens=50,  # 생성될 최대 토큰 수
    )

    # 응답에서 생성된 텍스트 출력
    return response.choices[0].message["content"].strip()


def ChatGPT2(input_msg):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 사용할 엔진 선택 (gpt
        messages=[
            {
                "role": "system",
                "content": "Convert Korean words to English.",
            },
            {
                "role": "system",
                "content": "in the form of word1, word2, word3, word4, word5.",
            },
            {"role": "user", "content": input_msg},
        ],
        max_tokens=50,  # 생성될 최대 토큰 수
    )

    # 응답에서 생성된 텍스트 출력
    return response.choices[0].message["content"].strip()
