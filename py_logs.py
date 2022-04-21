from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN = getenv("TOKEN")
client_id = getenv("client_id")
client_secret = getenv("client_secret")
user_agent = getenv("user_agent")
username = getenv("username")
password = getenv("password")
