import requests
import io


def process_cloudsight(img_url):
    # Image Captioning API URL 설정
    url = "https://image-caption-generator2.p.rapidapi.com/v2/captions/simple"

    # 이미지 URL을 querystring에 포함
    querystring = {"imageUrl": img_url}

    # RapidAPI 키 및 호스트 설정
    headers = {
        "X-RapidAPI-Key": "694e995e2dmshb5cd9dbdeb0ace2p1faaf4jsnbdef586d806b",
        "X-RapidAPI-Host": "image-caption-generator2.p.rapidapi.com",
    }

    # Image Captioning API 요청 및 응답
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # 요청이 실패했을 경우 예외 발생

    # 응답 출력
    print("되나? 왜 안 돼?", response.json())

    return response.json()
