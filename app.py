from flask import Flask, render_template, url_for


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/conference/')
def conference():
    return render_template('conference.html')

if __name__ == '__main__':
    app.run(debug=True)
