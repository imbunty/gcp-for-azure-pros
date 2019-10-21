from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def main():
    model = {"title": "Hello GCP Fans to Our Fantastic App!"}
    return render_template('index.html', model=model)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=int(os.environ.get('PORT', 8080)))
