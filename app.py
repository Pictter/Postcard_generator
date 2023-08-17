from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("./templates/main.html")

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('name')
    return f'안녕하세요, {name}님!'

if __name__ == '__main__':
    app.run()
