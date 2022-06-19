"""
Test suite for the whenday CLI tool
"""

from datetime import datetime
import pytest
from whenday import whenday


def test_date_only():
    """Test that date (w/o time) can be parsed and compared with its corresponding (same) time"""
    result = whenday("2022-06-01", datetime(2022,6,1,0,0))
    assert "datetime.timedelta(0)" == result

def test_date_time():
    """Test that date with time can be parsed and compared with its corresponding (same) time"""
    result = whenday("2022-06-01 13:37", datetime(2022,6,1,13,37))
    assert "datetime.timedelta(0)" == result


if __name__ == '__main__':  # pragma: no cover
    pytest.main()
