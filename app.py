from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return "hello world!"

@app.route('/user')
def index():
    return render_template("main.html")

@app.route('/letter', methods=['POST'])
def result():
    letter = request.form.get('letter')
    return f'''편지 보내주셔서 감사합니다!\
    {letter}'''

if __name__ == '__main__':
    app.run(debug=True)