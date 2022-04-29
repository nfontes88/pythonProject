import production
import pytest

@pytest.fixture
def_test_massachusetts_state():
    massachusetts = input.get_massachusetts_state()
    assert len(massachusetts)
