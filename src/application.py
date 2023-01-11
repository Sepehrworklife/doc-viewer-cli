from typer import Typer
from commands import register_commands
from utils import is_initial_happend

# Initial Application
app = Typer()
# Add all command to the application
register_commands(app=app)


@app.command()
@is_initial_happend
def test():
    print("Test")


if __name__ == "__main__":
    app()
