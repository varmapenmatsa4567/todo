from flask import Flask, url_for, redirect, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"

@app.route('/login',methods=['POST'])
def login():
    user = request.form['nm']
    return redirect(url_for('success',name=user))


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


if __name__ == '__main__':
    app.run()