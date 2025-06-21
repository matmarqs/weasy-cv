from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time, json
from typing import cast

TEMPLATE_DIR = "templates"
TEMPLATE_NAME = "resume.html"
DATA_FILE = "data/cyber.json"
STYLESHEET = "static/style.css"
OUTPUT_FILE = "resume.pdf"
WATCH_EXTENSIONS = (".html", ".json", ".css", ".png", ".jpg", ".jpeg", ".gif", ".svg")

class PDFBuilder(FileSystemEventHandler):
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        self.build_pdf()

    def on_modified(self, event):
        if cast(str, event.src_path).lower().endswith(WATCH_EXTENSIONS):
            print(f"Change detected in {event.src_path}, regenerating PDF...")
            self.build_pdf()

    def build_pdf(self):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Recarrega o template sempre
            template = self.env.get_template(TEMPLATE_NAME)
            html = template.render(**data)

            HTML(string=html, base_url=".").write_pdf(
                OUTPUT_FILE,
                stylesheets=[STYLESHEET]
            )
            print(f"PDF gerado: {OUTPUT_FILE}")
        except Exception as e:
            print("Erro ao gerar o PDF:", e)

if __name__ == "__main__":
    print("Preview live: watching for changes...")
    observer = Observer()
    observer.schedule(PDFBuilder(), path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
