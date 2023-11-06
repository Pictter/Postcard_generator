import requests
import io


def process_cloudsight():
    
    # Image Captioning API URL 설정
    url = "https://image-caption-generator2.p.rapidapi.com/v2/captions/simple"

    image_url = 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-zPeqUtMRN6nLu5uqYUchXyY0/user-CjD68zBxthShLHUFKiT86O9z/img-reB2scjT8lbfxgPNonhz9Onf.png?st=2023-11-05T00%3A43%3A35Z&se=2023-11-05T02%3A43%3A35Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-11-04T04%3A09%3A13Z&ske=2023-11-05T04%3A09%3A13Z&sks=b&skv=2021-08-06&sig=dmue3yTUpGS4iygWgMQUF7Nq%2Bwuk1sF10b60RCROOag%3D'

    # 이미지 URL을 querystring에 포함
    querystring = {"imageUrl": image_url}
    
    # RapidAPI 키 및 호스트 설정
    headers = {
        "X-RapidAPI-Key": '694e995e2dmshb5cd9dbdeb0ace2p1faaf4jsnbdef586d806b',
        "X-RapidAPI-Host": "image-caption-generator2.p.rapidapi.com"
    }

    # Image Captioning API 요청 및 응답
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # 요청이 실패했을 경우 예외 발생

    # 응답 출력
    print(response.json())

process_cloudsight()
