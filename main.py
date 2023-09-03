from plugin.db_utils import attempt_init_db
from plugin.consts import (
    BIND_ADDRESS,
    BIND_PORT,
    CONFIG_DIRECTORY,
    DATA_DIRECTORY,
    EXTERNAL_URL
)
from plugin.server import LocalAudioHandler
import http
import threading

if __name__ == "__main__":
    print("\nUsing configuration:")
    print(f"- BIND_ADDRESS: {BIND_ADDRESS}")
    print(f"- BIND_PORT: {BIND_PORT}")
    print(f"- EXTERNAL_URL: {EXTERNAL_URL}")
    print(f"- DATA_DIRECTORY: {DATA_DIRECTORY}")
    print(f"- CONFIG_DIRECTORY: {CONFIG_DIRECTORY}")
    print("\nInitializing database...")
    attempt_init_db()
    print(f"Database is initialized, server will now start...")
    server = http.server.ThreadingHTTPServer((BIND_ADDRESS, BIND_PORT), LocalAudioHandler)
    server.serve_forever()
