from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/about")
def about():
    return "Ceci est la page À propos !"  # Fransızca sayfa

@app.route("/contact")
def contact():
    return ("Telephone number : ")


@app.route("/delete/item")

def delete():
    return "delete item"

@app.route("/delete/<string:id>")
def delete_id(id):
    return f" id : {id}"


if __name__ == "__main__":
    app.run(debug=True)
