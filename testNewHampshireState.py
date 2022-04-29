import production
import pytest

@pytest.fixture
def_test_new_hampshire_state():
    new_hampshire = input.get_new_hampshire_state()
    assert len(new_hampshire)