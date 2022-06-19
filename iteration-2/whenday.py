"""
whenday - the tool you never though you would need (and probably never will)
"""

import sys
from datetime import datetime

def whenday(date_string):
    """Main function for the whenday CLI took"""
    return repr(datetime.fromisoformat(date_string))

if __name__ == '__main__': # pragma: no cover
    print(whenday(sys.argv[1]))
