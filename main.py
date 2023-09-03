from plugin.db_utils import attempt_init_db
from plugin.consts import BIND_ADDRESS, BIND_PORT
from plugin.server import LocalAudioHandler
import http
import threading

if __name__ == "__main__":
    print("Initializing database...")
    attempt_init_db()
    print("Starting server...")
    server = http.server.ThreadingHTTPServer((BIND_ADDRESS, BIND_PORT), LocalAudioHandler)
    server.serve_forever()