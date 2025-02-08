from configparser import ConfigParser


CONFIG_FILE = 'config.ini'


def getConfig():
    """
    Method that create a ConfigParser object and returns it

    Returns:
        config (ConfigParser)
    """
    config = ConfigParser()
    config.read(CONFIG_FILE)

    return config

