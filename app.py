from flask import Flask, render_template
app = Flask(__name__)

application = app # our hosting requires application in passenger_wsgi

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/plant1")
def plant1():
    return render_template("plant1.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
      app.run('localhost', 5000, debug=True)