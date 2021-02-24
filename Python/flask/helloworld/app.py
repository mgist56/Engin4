from flask import Flask

# this makes a new flask app called "app"
app = Flask(__name__)

@app.route("/")
def hello_world():
     return "hello world!"

if __name__ == "__main__":
     # this runs the app and returns "hello world"
     app.run(host="0.0.0.0", port=80)