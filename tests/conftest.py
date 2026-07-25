import os
import tempfile
import pytest
from markrethe import Markrethe


@pytest.fixture
def markrethe():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Markrethe(tmpdir), tmpdir


@pytest.fixture
def read_log():
    def _read(tmpdir):
        with open(os.path.join(tmpdir, "log.md")) as f:
            return f.read()

    return _read
