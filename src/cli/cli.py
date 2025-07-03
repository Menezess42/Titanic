import click
import pandas as pd


def analyze_data(*args, **kwargs):
    """
    """
    if args:
        data = args[0]
        n = args[1]
        file = None

    elif kwargs:
        file = kwargs.fromkeys("file")

    if file:
        df = pd.read_csv(file)
        click.echo("DataFrame loaded. Here's the head:")
        click.echo(df.head().to_string())  # to_string() for better console display
        click.echo("\n\n")

    elif not data.empty:
        click.echo("DataFrame loaded. Here's the head:")
        click.echo(data.head().to_string())  # to_string() for better console display
        click.echo("\n\n")

    else:
        click.echo("Please provide a CSV file using --file.")


if __name__ == "__main__":
    analyze_data()
