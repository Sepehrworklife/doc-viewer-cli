from typer import Typer
from commands import register_commands

# Initial Application
app = Typer()
# Add all command to the application
register_commands(app=app)


if __name__ == "__main__":
    app()
