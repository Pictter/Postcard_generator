# -*- coding:utf-8 -*-
import urllib3
import json


def Etri(input_msg):
    openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"

    openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU_spoken"

    accessKey = "b95093b2-4d5c-4976-841a-3d8d725efeb7"
    analysisCode = "ner"
    text = input_msg

    requestJson = {"argument": {"text": text, "analysis_code": analysisCode}}

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={
            "Content-Type": "application/json; charset=UTF-8",
            "Authorization": accessKey,
        },
        body=json.dumps(requestJson),
    )

    print("[responseCode] " + str(response.status))
    print("[responBody]")
    print(str(response.data, "utf-8"))
    # response.data를 UTF-8 문자열로 디코딩 -> Json으로 변환
    response_data_str = response.data.decode("utf-8")

    # 디코딩된 문자열을 JSON으로 파싱
    response_data_json = json.loads(response_data_str)
    morp_list = response_data_json["return_object"]["sentence"][0]["morp"]

    # 명사만 추출합니다. (품사가 'NNG', 'NNP', 'NNB', 'NR', 'NP' 인 경우)
    morp_list = [
        morp
        for morp in morp_list
        if morp["type"] in ("NNG", "NNP", "NNB", "NR", "NP", "")
    ]

    # morp_list = [morp for morp in morp_list if morp['type'] not in ('EC','SF','VC')]

    # 'weight' 키에 따라 morp_list 정렬 (내림차순)
    sorted_morp_list = sorted(morp_list, key=lambda x: x["weight"], reverse=True)

    sorted_morp_list = [morp["lemma"] for morp in sorted_morp_list]

    sorted_morp_list = list(set(sorted_morp_list))

    sorted_morp_list[:20]

    return sorted_morp_list
