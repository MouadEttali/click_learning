import click


all_colors = (
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "bright_black",
    "bright_red",
    "bright_green",
    "bright_yellow",
    "bright_blue",
    "bright_magenta",
    "bright_cyan",
    "bright_white",
)


@click.command()
def cli():
    """This script prints some colors. It will also automatically remove
    all ANSI styles if data is piped into a file.

    Give it a try!
    """
    for color in all_colors:
        click.secho(click.style(f"I am colored {color}", fg=color, bg="cyan"))
    for color in all_colors:
        click.secho(click.style(f"I am colored {color} and bold", fg=color, bold=True))
    for color in all_colors:
        click.secho(click.style(f"I am reverse colored {color}", fg=color, reverse=True))

    click.secho(click.style("I am blinking", blink=True))
    click.secho(click.style("I am underlined", strikethrough=True))