import openai

# OpenAI API 키 설정
api_key = "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"
openai.api_key = api_key

# ChatGPT API 호출

def ChatGPT(input_msg):
    final_msg = input_msg + "\n Pick 3 keywords from this message and return the results in English."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 사용할 엔진 선택 (gpt
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": final_msg}
        ],
        max_tokens=50,  # 생성될 최대 토큰 수
    )

# 응답에서 생성된 텍스트 출력
    print(response.choices[0].message['content'].strip())

ChatGPT("난 너를 사랑해 i love you girl 세상은 너 뿐이야. 소리쳐 부르지만 저 대답없는 노을만 붉게 타는데.")