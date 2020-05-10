import click


def info(msg):
    click.echo(msg)

def error(msg):
    click.echo(click.style(msg, fg="red"))
