import click


@click.group()
@click.version_option()
def cli():
    """Naval Fate.

    This is the docopt example adopted to Click but with some actual
    commands implemented and not just the empty parsing which really
    is not all that interesting.
    """


@cli.group(add_help_option=False)
@click.help_option('--help', '-h', help='Show my better message and exit')
def ship():
    """Manages ships."""


@ship.command("new")
@click.argument("name")
@click.argument("x", type=float)
@click.argument("y", type=float)
@click.argument('out', type=click.File('a'), default='ships.txt')
def ship_new(name, x, y, out):
    """Creates a new ship."""
    click.echo(f"Created ship {name}")
    click.echo(f"ship {name} in position {x}, {y}",file=out)
    
@ship.command("list")
@click.argument('input', type=click.File('r'), default="ships.txt")
def list(input):
    """lists all ships."""
    for f in input:
        click.echo(f)


@ship.command("move")
@click.argument("ship")
@click.argument("x", type=float)
@click.argument("y", type=float)
@click.argument('input', type=click.File('r'), default="ships.txt")
@click.option("--speed", metavar="KN", default=10, help="Speed in knots.")
def ship_move(ship, x, y, speed,input):
    """Moves SHIP to the new location X,Y."""
    for f in input:
        if ship in f:
            click.echo(f"Moving ship {ship} to {x},{y} with speed {speed}")


@ship.command("shoot")
@click.argument("ship")
@click.argument("x", type=float)
@click.argument("y", type=float)
def ship_shoot(ship, x, y):
    """Makes SHIP fire to X,Y."""
    click.echo(f"Ship {ship} fires to {x},{y}")


@cli.group("mine")
def mine():
    """Manages mines."""


@mine.command("set")
@click.argument("x", type=float)
@click.argument("y", type=float)
@click.option(
    "ty",
    "--moored",
    flag_value="moored",
    default=True,
    help="Moored (anchored) mine. Default.",
)
@click.option("ty", "--drifting", flag_value="drifting", help="Drifting mine.")
def mine_set(x, y, ty):
    """Sets a mine at a specific coordinate."""
    click.echo(f"Set {ty} mine at {x},{y}")


@mine.command("remove")
@click.argument("x", type=float)
@click.argument("y", type=float)
def mine_remove(x, y):
    """Removes a mine at a specific coordinate."""
    click.echo(f"Removed mine at {x},{y}")