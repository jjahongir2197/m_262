from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        note = request.form["note"]
        notes.append(note)
        return redirect("/")

    return render_template("notes.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)
