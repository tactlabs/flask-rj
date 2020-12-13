
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():

    return "helloworld"

@app.route("/main")
def main2():

    return "helloflask"


if __name__ == "__main__":
    app.run(debug=True,port=3000)
