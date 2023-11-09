from flask import Flask, request, render_template, session, send_file, render_template
from ChatGPT import ChatGPT, ChatGPT2
from DALLE2 import dalle
import urllib.request
from Etri import Etri
from image_text import process_cloudsight

from _auth import random_string, md5_hash

app = Flask(__name__)

app.secret_key = md5_hash(random_string(32))


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/letter", methods=["POST"])
def letter():
    letter_text = request.form.get("letter")
    print("letter_text", letter_text)
    keyword = Etri(letter_text)
    ##keyset = "".join(Etrikey)
    # keyword = ChatGPT(letter_text + keyset).split(", ")
    print("keyword", keyword)

    session["input_text_"] = letter_text
    session["keyword_"] = keyword  # 세션에 값을 저장
    return render_template("letter.html", keyword=keyword)


@app.route("/image", methods=["GET"])
def img():
    keyword = session.get("keyword_")
    input_text_ = session.get("input_text_")
    # print("input_text", input_text_)
    newkeyworld = ChatGPT2("".join(keyword)).split(", ")

    image_response = dalle(newkeyworld)
    image_url = []
    for i in range(0, 3, 1):
        image_url.append(image_response["data"][i]["url"])

    print("image_url", image_url)
    return render_template("image.html", image_url=image_url, letter=input_text_)


@app.route("/selected-image", methods=["POST"])
def selected_image():
    data = request.json
    img_src = data["imgSrc"]
    session["image_url_"] = img_src
    textres = process_cloudsight(img_src)
    text = textres["caption"]
    print(text)

    return render_template(
        "selected-image.html",
        image_url=img_src,
        letter=session["input_text_"],
        text=text,
    )


@app.route("/test", methods=["GET"])
def test_html():
    return render_template(
        "test.html",
        image_url="https://i.namu.wiki/i/SLLmySVvTaIb51ygri4wwte51MZEOcfmdQUnMz3TnNPdYEuQM80Wgn3pONY1mBon0GIaZyvmowwqm8JEHGHDkw.webp",
        letter="아무거나 써볼게요",
        text="설명입니다",
    )


if __name__ == "__main__":
    app.run(debug=True)
