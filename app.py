from flask import Flask, render_template, request, redirect
import re
import os

app = Flask(__name__)

# Create users.txt if it doesn't exist
if not os.path.exists("users.txt"):
    open("users.txt", "w").close()


# Email validation function
def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return "Email or password missing"

        if not valid_email(email):
            return "Invalid email format"

        # Save email and password
        with open("users.txt", "a") as f:
            f.write(f"{email},{password}\n")

        return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/admin")
def admin():

    users = []

    with open("users.txt", "r") as f:
        users = f.readlines()

    return render_template("admin.html", users=users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
