from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = '../static'


@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return render_template('greeting.html',
                           say=request.form['say'], to=request.form['to'], campus=request.form['campus'])


if __name__ == '__main__':
    app.run()
