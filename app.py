from flask import Flask, request, render_template
from ChatGPT import ChatGPT
from DALLE2 import dalle

app = Flask(__name__)
keyword=""

@app.route('/')
def root():
    return "hello world!"

@app.route('/user')
def index():
    return render_template("main.html")

@app.route('/letter', methods=['POST'])
def letter():
    letter = request.form.get('letter')
    global keyword 
    keyword = ChatGPT(letter)
    image = dalle(keyword)
    print(image)
    return render_template("letter.html",keyword=keyword)

@app.route('/image')
def img():
    global keyword
    



if __name__ == '__main__':
    app.run(debug=True)