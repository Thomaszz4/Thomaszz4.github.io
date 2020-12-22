from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def access():
    return render_template('check.html')

@app.route('/check', methods=['POST'])
def check():
    if request.form.get('password') == 'zhuzhu520':
        return render_template('index.html')
    else:
        return render_template('check_wrong.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/main.html')
def main():
    return render_template('main.html')

@app.route('/add_successfully', methods=['POST'])
def add_comment():
    with open('/Users/huangqiming/Desktop/html/Thomaszz4.github.io/comments.txt', 'w') as fr:
        fr.write(request.form.get('message'))
    return "Successfully add comments"

@app.route('/comment.html')
def comment():
    return render_template('comment.html')

@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/reference.html')
def reference():
    return render_template('reference.html')

@app.route('/note.html')
def note_():
    return render_template('note.html')

@app.route('/log.html')
def log():
    return render_template('log.html')

@app.route('/errors.html')
def errors():
    return render_template('errors.html')

if __name__ == '__main__':
    app.run()