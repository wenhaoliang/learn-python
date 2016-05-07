#!e:\practice\learn-python\django\django\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bpython==0.15','console_scripts','bpython-urwid'
__requires__ = 'bpython==0.15'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('bpython==0.15', 'console_scripts', 'bpython-urwid')()
    )
