from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time, json, os, argparse

TEMPLATE_DIR = "templates"
TEMPLATE_NAME = "resume.html"
STYLESHEET = "templates/global.css"
FONTAWESOME = "assets/fontawesome/css/all.min.css"
DEFAULT_OUTPUT = "resume.pdf"
WATCH_EXTENSIONS = (".html", ".json", ".css", ".png", ".jpg", ".jpeg", ".gif", ".svg")
IGNORE_DIRS = ["assets/fontawesome"]

class PDFBuilder(FileSystemEventHandler):
    def __init__(self, data_file: str, output_file: str) -> None:
        self.data_file = data_file
        self.output_file = output_file
        self.env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        self.build_pdf()

    def on_modified(self, event) -> None:
        path = str(os.path.normpath(event.src_path))  # Cast explícito para str
        if any(ignored in path for ignored in IGNORE_DIRS):
            return
        if path.lower().endswith(WATCH_EXTENSIONS):
            print(f"Change detected in {path}, regenerating PDF...")
            self.build_pdf()

    def build_pdf(self) -> None:
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            template = self.env.get_template(TEMPLATE_NAME)
            html = template.render(**data)

            HTML(string=html, base_url=".").write_pdf(
                self.output_file,
                stylesheets=[STYLESHEET, FONTAWESOME]
            )
            print(f"PDF successfully generated: {self.output_file}")
        except Exception as e:
            print("Error generating PDF:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate PDF resume from JSON data')
    parser.add_argument('--json', '-j', 
                       required=True,
                       help='Path to JSON data file (required)')
    parser.add_argument('--output', '-o',
                       default=DEFAULT_OUTPUT,
                       help=f'Output PDF filename (default: {DEFAULT_OUTPUT})')
    args = parser.parse_args()

    print(f"Preview live: watching for changes...")
    print(f"Using data file: {args.json}")
    
    observer = Observer()
    observer.schedule(PDFBuilder(args.json, args.output), path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
