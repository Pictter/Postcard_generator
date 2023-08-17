import openai
import requests

openai.api_key = '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'

user_prompt = "love warm "
add_prompt = "background"
input_prompt=user_prompt+add_prompt
response = openai.Image.create(
    prompt=input_prompt,
    n=3,
    size="1024x1024",
    response_format="url"
)


image_url1 = response['data'][0]['url']
image_url2 = response['data'][1]['url']
image_url3 = response['data'][2]['url']

print(image_url1)
print(image_url2)
print(image_url3)