#!e:\practice\learn-python\django\django\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pygments==2.1.3','console_scripts','pygmentize'
__requires__ = 'pygments==2.1.3'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pygments==2.1.3', 'console_scripts', 'pygmentize')()
    )
