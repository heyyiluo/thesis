#! /usr/bin/env python
import click
from flask.cli import FlaskGroup
from thesisweb import create_app


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """Management script for application."""


if __name__ == '__main__':
    cli()
