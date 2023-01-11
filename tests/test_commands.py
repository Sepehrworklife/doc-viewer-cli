from src.application import app
import pytest
from src.constants import SEC_FILE_NAME
from typer.testing import CliRunner
import os

runner = CliRunner()


def test_init_error():
    if os.path.exists(SEC_FILE_NAME):
        os.remove(SEC_FILE_NAME)
    result = runner.invoke(app, ["test"])
    assert "ERROR!" in result.stdout


def test_init_command():
    result = runner.invoke(app, ["init"], input="faketoken")
    assert "Success" in result.stdout
    assert os.path.exists(SEC_FILE_NAME) == True
