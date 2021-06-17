from flask import Flask, render_template, request

from utils.fibonacci import fibonacci

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("basicform.html")


@app.route("/welcome/<string:name>")
def welcome(name):
    heading_template = render_template("heading.txt", user=name)
    return render_template("basicform.html", heading=heading_template)


@app.route("/welcome")
def welcome_null():
    return "WELCOME!!"


@app.route("/isnewyear")
def isNewYear():
    isIt = False
    return render_template("isNewYear.html", bool=isIt)


@app.route("/bye")
def bye_null():
    return bye('')


@app.route("/fibonacci<int:number>")
def fib(number):
    return f"{fibonacci(number)}"


@app.route("/loop<int:number>")
def loop(number):
    return render_template("loop.html", number=number)


@app.route("/input")
def form_input():
    return render_template("formtemplate.html", heading="Hi!! This is form demo.. Enjoy. :)")


@app.route("/form", methods=["POST"])
def form():
    name = request.form.get("name")
    password = request.form.get("password")
    return render_template("greeting.html", name=name, password=password)


@app.route("/bye/<string:name>")
def bye(name):
    if name != '':
        name = " " + name
    heading_template = render_template("bye.txt", user=name)
    return render_template("basicform.html", heading=heading_template)
