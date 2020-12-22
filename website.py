from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('check.html')

@app.route('/check', methods=['POST'])
def check():
    if request.form.get('password') == 'zhuzhu520':
        return render_template('index.html')

@app.route('/index.html')
def add():
    return render_template('index.html')

@app.route('/add_successfully', methods=['POST'])
def add_comment():
    with open('/Users/huangqiming/Desktop/web/comments.txt', 'w') as fr:
        fr.write(request.form.get('message'))
    return "Successfully add comments"
