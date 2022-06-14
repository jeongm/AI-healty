from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main_user(user):
    # after login
    return render_template('index2.html',name=user)

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/write')
def write():
    return render_template('write.html')


if __name__ == '__main__':
    app.run(debug=True)