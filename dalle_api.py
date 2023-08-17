import openai
import requests

url = "http://localhost:5000/send"
openai.api_key = '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'

response = openai.Image.create(
    prompt="awesome cat",
    n=1,
    size="1024x1024",
    response_format="b64_json"
)

image_url = response['data'][0]['b64_json']
response = requests.post(url, data={"text_data": image_url})
if response.status_code == 200:
    print("서버 응답:", response.text)