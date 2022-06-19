"""
Test suite for the whenday CLI tool
"""

import pytest
from whenday import whenday


def test_date_only():
    """Test that date (w/o time) can be parsed"""
    result = whenday("2022-06-01")
    assert "datetime.datetime(2022, 6, 1, 0, 0)" == result

def test_date_time():
    """Test that date with time can be parsed"""
    result = whenday("2022-06-01 13:37")
    assert "datetime.datetime(2022, 6, 1, 13, 37)" == result

if __name__ == '__main__':  # pragma: no cover
    pytest.main()
