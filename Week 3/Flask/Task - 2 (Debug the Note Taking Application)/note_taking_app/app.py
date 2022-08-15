from glob import glob
from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        # note = request.args.get("note")
        note = request.form["note"]
        if note != None and note != "" and note not in notes:
            notes.append(note)
        return render_template("home.html", notes=notes)
    return render_template("home.html")
    

if __name__ == '__main__':
    app.run(debug=True)