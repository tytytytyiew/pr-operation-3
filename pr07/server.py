#!/usr/bin/env python3
import http.server
import socketserver
import json
import datetime
import os

PORT = 8080

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            
            data = {
                "status": "online",
                "server": "Python OS Course Server",
                "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "user": "Barsbek"
            }
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))
        else:
            # Возвращаем стандартную страницу или перенаправляем на index.html
            super().do_GET()

def run():
    server_address = ("", PORT)
    with socketserver.TCPServer(server_address, CustomHandler) as httpd:
        print(f"[*] Веб-сервер запущен на http://localhost:{PORT}")
        print("[*] Нажми Ctrl+C для остановки сервера.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[*] Сервер остановлен пользователем.")

if __name__ == "__main__":
    run()
