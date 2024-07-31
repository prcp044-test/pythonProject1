import configparser


def get_config():
    con = configparser.ConfigParser ()
    con.read('C:/My Floder/Python/GlobalLogic/pythonProject1/utilities/properties.ini')
    return con
