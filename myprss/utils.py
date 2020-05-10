from myprss.config import Config


def list_known_feeds():
    config = Config()
    return list(config["registry"].keys())
