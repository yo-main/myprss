import click

from src.registry import registry

# echo -e '\e]8;;http://example.com\aThis is a link\e]8;;\a'


@click.group()
def cli():
    pass


cli.add_command(registry)


if __name__ == "__main__":
    cli()
