import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print("Got Post")
        email = request.form["email"]
        contact_name = request.form["name"]
        text_content = request.form["text"]
        print(email)
        print(contact_name)
        print(text_content)
        print("Handle Post")
    return render_template("contact.html")



if __name__ == '__main__':
    app.run(host=os.environ.get('IP', "0.0.0.0"),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)