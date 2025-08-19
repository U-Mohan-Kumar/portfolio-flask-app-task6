# Flask Portfolio Website

A minimal personal portfolio built with **Flask**, **HTML**, and **CSS**.

## Features
- Home page shows About + Projects (rendered via Jinja2)
- Contact page with POST form and flash message
- Clean CSS in `/static/style.css`
- Templates in `/templates`

## Run Locally
```bash
# (Windows PowerShell)
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py

# (macOS / Linux)
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

Open http://127.0.0.1:5000/

## GitHub
```bash
git init
git branch -M main
git add .
git commit -m "Initial commit - Flask Portfolio"
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```
