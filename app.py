from flask import Flask, request, render_template, session, send_file, render_template
from ChatGPT import ChatGPT
from DALLE2 import dalle
import urllib.request

from _auth import random_string, md5_hash

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

@app.route('/download')
def download():
    url = request.args.get('image_url')  
    # url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-udHcUVpfVyx2Nt3o462FR5QA/user-m6jgVNuFOIGosEsQ3NG9sPgk/img-8Be3GGC778CWmd2Ef4fiKO8D.png?st=2023-08-17T19%3A57%3A28Z&se=2023-08-17T21%3A57%3A28Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-08-17T17%3A53%3A08Z&ske=2023-08-18T17%3A53%3A08Z&sks=b&skv=2021-08-06&sig=5DvvsgJSRVVAM4CwlQB2ccs4OkgaGzoSqkzLDwEXMwA%3D"
    urllib.request.urlretrieve(url, "test.jpg")


if __name__ == "__main__":
    app.run(debug=True)
