"""
Talk to Aliens
"""

import re
import sys

def main():
    """
    Main function
    """
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}', line):
            print(line)

if __name__ == '__main__':
    main()