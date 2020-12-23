import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet')

def hello(count, name):
    """Usage: cli.py [OPTIONS] LOCATION

  A little weather tool that shows you the current weather in a LOCATION of
  your choice. Provide the city name and optionally a two-digit country
  code. Here are two examples:

  1. London,UK

  2. Canmore

  You need a valid API key from OpenWeatherMap for the tool to work. You can
  sign up for a free account at https://openweathermap.org/appid."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()




# import click

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)

# if __name__ == '__main__':
#     hello()