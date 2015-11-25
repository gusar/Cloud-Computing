from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index File\n"

@app.route("/hello")
def hello():
    return "Hello World\n"

@app.route("/user/<username>")
def profile(username):
    return "User " + username + "\n"

@app.route("/post/<num>")
def post(num):
    return "Post " + num + "\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
