"""
whenday - the tool you never though you would need (and probably never will)
"""

import sys
from datetime import datetime

def whenday(date_string, now):
    """Main function for the whenday CLI took"""
    input_time = datetime.fromisoformat(date_string)
    delta_time = input_time - now
    return repr(delta_time)

if __name__ == '__main__': # pragma: no cover
    print(whenday(sys.argv[1], datetime.today()))
