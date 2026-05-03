#!/usr/bin/env python3
"""Character layer composer server.

Usage: python3 server.py [port]
Default port: 8080
"""
import http.server
import json
import os
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/folders":
            folders = sorted(
                d.name
                for d in ROOT.iterdir()
                if d.is_dir() and not d.name.startswith(".")
            )
            self._send_json(folders)

        elif path == "/api/images":
            qs = urllib.parse.parse_qs(parsed.query)
            folder = qs.get("folder", [""])[0]
            folder_path = ROOT / folder
            if not folder_path.is_dir():
                self.send_error(404, "Folder not found")
                return
            images = sorted(
                f.name for f in folder_path.iterdir() if f.suffix.lower() == ".png"
            )
            self._send_json(images)

        elif path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(ROOT / "index.html", "rb") as f:
                self.wfile.write(f.read())

        else:
            super().do_GET()

    def _send_json(self, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass  # suppress access log noise


if __name__ == "__main__":
    import socketserver

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    os.chdir(ROOT)

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serving at http://localhost:{port}")
        print(f"Root: {ROOT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nDone.")
