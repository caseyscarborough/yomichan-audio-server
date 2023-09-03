import os
from typing import Final

BIND_ADDRESS: Final = os.environ.get('BIND_ADDRESS', '0.0.0.0')
BIND_PORT: Final = int(os.environ.get('BIND_PORT', '5050'))
EXTERNAL_URL: Final = os.environ.get('EXTERNAL_URL', f"http://{BIND_ADDRESS}:{BIND_PORT}")
DATA_DIRECTORY: Final = os.environ.get('DATA_DIRECTORY', '/data')
CONFIG_DIRECTORY: Final = os.environ.get('CONFIG_DIRECTORY', DATA_DIRECTORY)
DB_FILE_NAME: Final = f"{DATA_DIRECTORY}/entries.db"
ANDROID_DB_FILE_NAME: Final = f"{DATA_DIRECTORY}/android.db"
DB_VERSION_FILE_NAME: Final = f"{DATA_DIRECTORY}/entries_version.txt"
JMDICT_FORMS_JSON_FILE_NAME: Final = f"{DATA_DIRECTORY}/jmdict_forms.json"
DEFAULT_CONFIG_FILE_NAME: Final = "config.default.json"
CONFIG_FILE_NAME: Final = f"{CONFIG_DIRECTORY}/config.json"
LATEST_VERSION_FILE_NAME: Final = "version.txt"

ROWID: Final = 0
EXPRESSION: Final = 1
READING: Final = 2
SOURCE: Final = 3
SPEAKER: Final = 4
DISPLAY: Final = 5
FILE: Final = 6
