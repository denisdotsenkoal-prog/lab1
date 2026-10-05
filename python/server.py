from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

PORT = 3002

BASE_DIR = Path(__file__).resolve().parent / "public"

FILES = {
    "/": (BASE_DIR / "index.html").read_bytes(),
    "/about": (BASE_DIR / "about.html").read_bytes(),
    "/404": (BASE_DIR / "404.html").read_bytes(),
    "/styles.css": (BASE_DIR / "styles.css").read_bytes(),
}

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        pathname = parsed_url.path

        status_code = 200
        content_type = "text/html; charset=utf-8"

        if pathname == "/":
            content = FILES["/"]
        elif pathname == "/about":
            content = FILES["/about"]
        elif pathname == "/styles.css":
            contentType = "text/css; charset=utf-8"
            content_type = "text/css; charset=utf-8"
            content = FILES["/styles.css"]
        else:
            status_code = 404
            content = FILES["/404"]

        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()

        self.wfile.write(content)

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]}")

def run():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Python сервер запущено на http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер зупинено.")

if __name__ == "__main__":
    run()