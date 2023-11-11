from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>hello world</p>"

@app.route("/home")
def home_page():
    return "<h1>Welcome to my first flask website</h1>"

if __name__ =="__main__":
    app.run(debug = True)