import click

@click.group()
def freddys():
    pass

@freddys.group()
def lunch():
    pass


@freddys.group()
def dinner():
    pass

@click.command()
def burger():
    click.echo(f"Enjoy your burger")


lunch.add_command(burger)
dinner.add_command(burger)
