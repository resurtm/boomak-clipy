#!/usr/bin/env python
import click


@click.group()
@click.option('--verbose', is_flag=True)
def cli(verbose):
    """Boomak bookmarking service CLI client."""
    click.echo('Hello, world!')


register_password_help = '''Password to be used for your new user account. Required option.'''


@cli.command()
@click.argument('username')
@click.argument('email')
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True, help=register_password_help)
def register(username, email, password):
    """Create a new user account."""
    click.echo('Password is: {}'.format(password))


@cli.command()
@click.argument('username')
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def login(username, password):
    """Sign into your existing account."""
    click.echo('Password is: {}'.format(password))


if __name__ == '__main__':
    cli()
