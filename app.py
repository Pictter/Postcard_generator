from flask import Flask, request, render_template, session
from ChatGPT import ChatGPT
from DALLE2 import dalle

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

@app.route("/")
def root():
    return "hello world!"


@app.route("/user")
def index():
    return render_template("main.html")

@app.route('/letter', methods=['POST'])
def letter():
    letter_text = request.form.get("letter")
    keyword = ChatGPT(letter_text)
    session["input_text_"] = letter_text
    session["keyword_"] = keyword  # 세션에 값을 저장
    return render_template("letter.html", keyword=keyword)


@app.route('/image', methods=['GET'])
def img():
    keyword = session.get("keyword_")
    input_text_ = session.get("input_text_")
    image_response = dalle(keyword)
    image_url = []
    for i in range(0, 3, 1):
        image_url.append(image_response["data"][i]["url"])
    return render_template("image.html", image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
