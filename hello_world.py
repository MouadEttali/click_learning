import click


class Info(object):
    def __init__(self) -> None:
        self.verbose = False
        self.home_directory = "."

pass_config = click.make_pass_decorator(Info, ensure=True)

@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home_directory', type=click.Path())

@pass_config
def say(config, verbose, home_directory):
    config.verbose=verbose
    config.home_directory=home_directory


@say.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--fname', prompt='Your firt name',
              help='The first name of person to greet.', default="Mouad")

@click.option('--lname', prompt='Your last name',
              help='The last name of person to greet.', default="Et-tali")
@click.argument('out', type=click.File('w'), default='-')
@pass_config
def hello(config, count, fname, lname, out):
    """Simple program that greets LNAME FNAME for a total of COUNT times.

    Args:
        -out output file

    """
    if config.verbose:
        click.echo("we are in verbose mode")
    click.echo(f"home directory is {config.home_directory}")
    for x in range(count):
        click.echo(f"Hello {lname} {fname}!",file=out)



