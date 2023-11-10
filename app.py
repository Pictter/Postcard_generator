from flask import Flask, request, render_template, session, send_file, render_template
from ChatGPT import ChatGPT2
from DALLE2 import dalle
import urllib.request
from Etri import Etri
from image_text import process_cloudsight
import googletrans
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
    print("keyword", keyword)
    session["input_text_"] = letter_text
    session["keyword_"] = keyword
    return render_template("letter.html", keyword=keyword)


@app.route("/image", methods=["GET"])
def img():
    keyword = session.get("keyword_")
    input_text_ = session.get("input_text_")
    newkeyworld = ChatGPT2("".join(keyword)).split(", ")
    translator = googletrans.Translator()

    image_response = dalle(newkeyworld)
    image_url = []
    image_des = []
    for i in range(0, 3, 1):
        image_url.append(image_response["data"][i]["url"])
        image_des.append(
            translator.translate(
                process_cloudsight(image_response["data"][i]["url"])["caption"],
                dest="ko",
            ).text
        )
    print("image_url", image_url)
    return render_template(
        "image.html", image_url=image_url, letter=input_text_, image_des=image_des
    )


@app.route("/selected-image", methods=["POST"])
def selected_image():
    translator = googletrans.Translator()
    data = request.json
    img_src = data["imgSrc"]
    imgdes = data["description"]
    session["image_url_"] = img_src

    return render_template(
        "selected-image.html",
        image_url=img_src,
        letter=session["input_text_"],
        text=imgdes,
    )


if __name__ == "__main__":
    app.run(debug=True)
