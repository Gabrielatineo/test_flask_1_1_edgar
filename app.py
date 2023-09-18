from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return {"payload":"hack-1 finished"}





if __name__ == "main":
    app.run(debug=True)
