import os

SERVER_IP = '172.23.0.2' # Listens on all interfaces
BIND_IP = '172.23.0.2' # IP for bots and users to connect to (change this)
BOT_PORT = 9132
COMMAND_PORT = 28156
WEB_PORT = 80
DB_URI = 'file:/path/to/pynet.db' # Location of database file, it will be created if it doesn't exist (change this)
PATH = os.path.dirname(__file__)
PUBLIC = os.path.join(PATH, 'public')