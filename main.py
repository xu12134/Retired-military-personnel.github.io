from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/education')
def activities():
    return render_template('education.html')

if __name__ == '__main__':
    app.run(debug=True)
    