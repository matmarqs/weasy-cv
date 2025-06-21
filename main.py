from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
import json
from pathlib import Path

# Load data from JSON
with open("data/cyber.json", "r") as f:
    data = json.load(f)

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("resume.html")

# Render HTML with data
rendered_html = template.render(**data)

# Generate PDF
HTML(string=rendered_html, base_url=".").write_pdf(
    "resume.pdf",
    stylesheets=["static/style.css"]
)

print("PDF generated: resume.pdf")
