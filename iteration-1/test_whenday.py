"""
Test suite for the whenday CLI tool
"""

import pytest
from whenday import whenday


def test_date_only():
    """Test that date (w/o time) can be parsed"""
    result = whenday("2022-06-01")
    assert "datetime.date(2022, 6, 1)" == result


if __name__ == '__main__':  # pragma: no cover
    pytest.main()
