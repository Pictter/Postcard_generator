
#-*- coding:utf-8 -*-
from flask import Flask, request
import urllib3
import json
import base64

app = Flask(__name__)

@app.route('/upload_audio', methods=['POST'])
def audio():
  print("upload_video가 들어감")
  file = request.files['audioFile']
  if file.filename == '':
      return "No selected file", 400

  audioContents = base64.b64encode(file.read()).decode("utf8")

  openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
  accessKey = "b95093b2-4d5c-4976-841a-3d8d725efeb7"
  audioFilePath = audioContents
  languageCode = "korean"
   
  file = open(audioFilePath, "rb")
  audioContents = base64.b64encode(file.read()).decode("utf8")
  file.close()
   
  requestJson = {    
      "argument": {
          "language_code": languageCode,
          "audio": audioContents
      }
  }
   
  http = urllib3.PoolManager()
  response = http.request(
      "POST",
      openApiURL,
      headers={"Content-Type": "application/json; charset=UTF-8","Authorization": accessKey},
      body=json.dumps(requestJson)
  )
   
  print("[responseCode] video " + str(response.status))
  print("[responBody]")
  print(str(response.data,"utf-8"))

  response_data_str = response.data.decode('utf-8')

    # 디코딩된 문자열을 JSON으로 파싱
  response_data_json = json.loads(response_data_str)
  return response_data_json
                                  