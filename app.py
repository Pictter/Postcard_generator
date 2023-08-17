from flask import Flask, request, render_template, session, send_file, render_template
from ChatGPT import ChatGPT
from DALLE2 import dalle
from _auth import random_string, md5_hash
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Image
import urllib.request
import io

app = Flask(__name__)

app.secret_key = md5_hash(random_string(32))

@app.route("/")
def root():
    return "hello world!"


@app.route("/user")
def index():
    return render_template("main.html")

@app.route('/letter', methods=['POST'])
def letter():
    letter_text = request.form.get("letter")
    keyword = ChatGPT(letter_text).split(', ')
    session["input_text_"] = letter_text
    session["keyword_"] = keyword  # 세션에 값을 저장
    return render_template("letter.html", keyword=keyword)


@app.route('/image', methods=['GET'])
def img():
    keyword = session.get("keyword_")
    input_text_ = session.get("input_text_")
    print(keyword)
    print(input_text_)
    image_response = dalle(keyword)
    image_url = []
    for i in range(0, 3, 1):
        image_url.append(image_response["data"][i]["url"])
    return render_template("image.html", image_url=image_url)

@app.route('/selected-image', methods=['POST'])
def selected_image():
    data = request.json
    img_src = data['imgSrc']
    session["image_url_"]=img_src
    
    return render_template("selected-image.html",image_url=img_src, letter = session["input_text_"] )

if __name__ == "__main__":
    app.run(debug=True)
