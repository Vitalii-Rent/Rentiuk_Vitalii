import pytest
from scenario import run_scenario


@pytest.fixture(scope="session")
def scenario():
    return run_scenario()


def test_addition(scenario):
    assert len(scenario[0]) > 0, 'Addition failed'


def test_deletion(scenario):
    assert len(scenario[1]) == 0, 'Deletion failed'
