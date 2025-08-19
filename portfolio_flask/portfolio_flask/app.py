from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev-secret"  # For flash messages (replace in production)

@app.route("/")
def home():
    projects = [
        {"title": "IoT Water Level Monitor", "desc": "ESP32 + flow sensors + LCD display", "url": "#"},
        {"title": "Flask To-Do App", "desc": "Simple CRUD app built with Flask", "url": "#"},
        {"title": "Cybersecurity Notes", "desc": "Common attacks & mitigations", "url": "#"},
    ]
    return render_template("index.html", projects=projects, year=datetime.now().year)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        # Normally you'd save to DB or send an email here
        flash(f"Thanks {name}! I'll reach you at {email}.")
        return redirect(url_for("contact"))
    return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
