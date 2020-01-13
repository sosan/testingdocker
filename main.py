from flask import Flask
from flask import render_template
app = Flask(__name__)
app.secret_key = "holal"

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run("127.0.0.1", 7050, debug=True)

