import click

from myprss import logger
from myprss.config import Config


@click.group("registry", help="Manage your list of rss feed")
def registry():
    pass


@registry.command("add", no_args_is_help=True, options_metavar="")
@click.argument("name", required=True)
@click.argument("url", required=True)
def register_new_feed(name, url):
    config = Config()
    config.data["registry"][name] = url
    config.save()
    logger.info(f"{name} has been added to the rss registry")


@registry.command("list")
def list_all_feed():
    config = Config()

    if not config.data["registry"]:
        logger.info("The registry is empty")
        return

    max_name_size = max(len(name) for name in config.data["registry"].keys())

    titles = f"{'NAME':{max_name_size}}\t| URL"

    logger.info(titles)
    for name, url in config.data["registry"].items():
        logger.info(f"{name:{max_name_size}}\t| {url}")


@registry.command("delete", no_args_is_help=True, options_metavar="")
@click.argument("name", required=True)
def delete_feed(name):
    config = Config()
    if name not in config.data["registry"]:
        logger.error(f"{name} is unknown")
        return

    del config.data["registry"][name]
    config.save()
    logger.info(f"{name} has been deleted from the rss registry")
