import openai

<<<<<<< HEAD
api_key = "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"

=======
# OpenAI API 키 설정
api_key = "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"
>>>>>>> 0738d54 (fix: API fix)
openai.api_key = api_key

# ChatGPT API 호출

def ChatGPT(input_msg):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 사용할 엔진 선택 (gpt
        messages=[
<<<<<<< HEAD
            {
                "role": "system",
                "content": "Look at the mood of this message, select 3 keywords, and return the results in English.",
            },
            {"role": "system", "content": "in the form of word1 word2 word3."},
            {"role": "user", "content": input_msg},
=======
            {"role": "system", "content": "Look at the mood of this message, select 3 keywords, and return the results in English."},
            {"role": "system", "content": "in the form of word1, word2, word3."},
            {"role": "user", "content": input_msg}
>>>>>>> 0738d54 (fix: API fix)
        ],
        max_tokens=20,  # 생성될 최대 토큰 수
    )

<<<<<<< HEAD
    # 응답에서 생성된 텍스트 출력
    return response.choices[0].message["content"].strip()

=======
# 응답에서 생성된 텍스트 출력
    return (response.choices[0].message['content'].strip())
>>>>>>> 0738d54 (fix: API fix)

ChatGPT("난 너를 사랑해 i love you girl 세상은 너 뿐이야. 소리쳐 부르지만 저 대답없는 노을만 붉게 타는데.")