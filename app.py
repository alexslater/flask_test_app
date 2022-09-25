from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key="cualquiercosa"

@app.route("/hello")

def index():
    flash("cual es tu nombre cabrito?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi" + str(request.form['name_input']) + ", holaa")
    return render_template("index.html")
    
