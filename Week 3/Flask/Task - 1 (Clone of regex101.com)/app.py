from distutils.log import debug
import re
from unittest import result
from flask import Flask, render_template, request
import re

app = Flask(__name__)

result = list()

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        global result
        result.clear()
        string = request.form.get("string")
        regex = request.form.get("regex")
        pattern = re.compile(regex)
        result = pattern.findall(string)
    return render_template("index.html", result = result)

if __name__ == "__main__":
    app.run(debug = True)