from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

places = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        place = request.form["place"]
        author = request.form["author"]
        description = request.form["description"]

        places.append({
            "place": place,
            "author": author,
            "description": description
        })

        return redirect(url_for("home"))

    return render_template("index.html", places=places)


if __name__ == "__main__":
    app.run(debug=True)