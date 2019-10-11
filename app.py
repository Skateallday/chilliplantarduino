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

@app.route("/plant2")
def plant2():
    return render_template("plant2.html")

if __name__ == "__main__":
      app.run('localhost', 5000, debug=True)