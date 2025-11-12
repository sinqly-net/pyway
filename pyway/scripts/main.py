import click

from pyway import settings
from pyway.info import Info
from pyway.log import logger
from pyway.migrate import Migrate
from pyway.validate import Validate


@click.group()
def cli():
    logger.info(settings.LOGO)


@cli.command()
@click.option('--db_ms', '-m', help='What database type to use. Options: postgres, oracle, mysql, sqlserver.')
@click.option('--host', '-h', help='Host to connect to.')
@click.option('--schema', '-s', help='Database schema to use.')
@click.option('--username', '-u', help='User to use when connecting.')
@click.option('--password', '-p', help='Users password.')
def migrate(db_ms: str = None, host: str = None, schema: str = None, username: str = None, password: str = None):
    logger.info('STARTING MIGRATE PROCESS . . .')
    if db_ms: settings.DBMS = db_ms
    if host: settings.DATABASE_URL = host
    if schema: settings.DATABASE_NAME = schema
    if username: settings.DATABASE_USERNAME = username
    if password: settings.DATABASE_PASSWORD = password
    Migrate(settings).run()
    logger.info('.MIGRATE ENDED.')


"""@cli.command()
def migrate():
    logger.info('STARTING MIGRATE PROCESS . . .')
    Migrate(settings).run()
    logger.info('.MIGRATE ENDED.')
"""


@cli.command()
def validate():
    logger.info('STARTING VALIDATE PROCESS . . .')
    Validate(settings).run()
    logger.info('.VALIDATE ENDED.')


@cli.command()
def info():
    logger.info('INFO . . .')
    Info(settings).run()
    logger.info('.INFO ENDED.')


if __name__ == '__main__':
    cli()
