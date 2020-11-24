from flask import Flask, render_template, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon_request():
    return send_from_directory("static/favicon","favicon.png")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)