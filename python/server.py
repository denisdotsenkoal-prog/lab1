from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlsplit

PORT = 3002
BASE = Path(__file__).resolve().parent

ROUTES = {
    "/": ("index.html", "text/html; charset=utf-8", 200),
    "/about": ("about.html", "text/html; charset=utf-8", 200),
    "/styles.css": ("styles.css", "text/css; charset=utf-8", 200),
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlsplit(self.path).path
        filename, content_type, status = ROUTES.get(
            path, ("404.html", "text/html; charset=utf-8", 404)
        )
        body = (BASE / "public" / filename).read_text(encoding="utf-8").encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    print(f"Python server: http://localhost:{PORT}")
    HTTPServer(("localhost", PORT), Handler).serve_forever()
