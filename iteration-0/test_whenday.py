"""
Test suite for the whenday CLI tool
"""

import pytest
from whenday import whenday


def test_tbd():
    """Just test the tooling setup"""
    result = whenday()
    assert "TBD" == result


if __name__ == '__main__':  # pragma: no cover
    pytest.main()
