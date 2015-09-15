import ConfigParser
from base64 import b64encode

def read_config():
    Config = ConfigParser.ConfigParser()
    Config.read("server.ini")
    return Config


def get_basic_auth():
    Config = read_config()
    username = Config.get('auth', 'username')
    password = Config.get('auth', 'password')
    basic_auth = b64encode(username + ':' + password)

    return basic_auth