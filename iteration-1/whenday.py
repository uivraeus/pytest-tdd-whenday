"""
whenday - the tool you never though you would need (and probably never will)
"""

import sys
from datetime import date

def whenday(date_string):
    """Main function for the whenday CLI took"""
    return repr(date.fromisoformat(date_string))

if __name__ == '__main__': # pragma: no cover
    print(whenday(sys.argv[1]))
