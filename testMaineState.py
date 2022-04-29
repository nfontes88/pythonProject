import production
import pytest

@pytest.fixture
def_test_maine_state():
    maine = input.get_maine_state()
    assert len(maine)