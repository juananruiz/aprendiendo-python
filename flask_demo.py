# Flask demo
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        initial_value = int(request.form['initial_value'])
        count = initial_value
    else:
        count = 0

    return render_template('/index.html', count=count)

@app.route('/increment')
def increment(count):
    count += 1
    return str(count)

@app.route('/decrement')
def decrement(count):
    count -= 1
    return str(count)

if __name__ == '__main__':
    app.run(debug=True)
