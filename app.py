import json
import random
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

QUOTES = [
    {"quote": "The only limit to our realization of tomorrow is our doubts of today.", "author": "Franklin D. Roosevelt"},
    {"quote": "In the middle of difficulty lies opportunity.", "author": "Albert Einstein"},
    {"quote": "Do one thing every day that scares you.", "author": "Eleanor Roosevelt"},
    {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
    {"quote": "It always seems impossible until it’s done.", "author": "Nelson Mandela"},
    {"quote": "Stay hungry, stay foolish.", "author": "Steve Jobs"},
]

class QuoteHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code: int, payload: dict):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path in ("/", "/quote"):
            quote = random.choice(QUOTES)
            self._send_json(200, quote)
        else:
            self._send_json(404, {"error": "Not Found"})

    # Silence default logging to keep output clean
    def log_message(self, format, *args):
        return


def run(host: str = "127.0.0.1", port: int = 8000):
    server = HTTPServer((host, port), QuoteHandler)
    print(f"Serving random quotes on http://{host}:{port}/quote")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    port_env = os.environ.get("PORT")
    try:
        port = int(port_env) if port_env else 8000
    except ValueError:
        port = 8000
    run(port=port)
