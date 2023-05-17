
from pytest import fixture


def pytest_addoption(parser):
    parser.addoption(
        "--token",
        action="store"
    )

