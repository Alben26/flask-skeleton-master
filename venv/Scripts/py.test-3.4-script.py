#!C:\Users\Admin\Downloads\flask-skeleton-master\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pytest==2.5.2','console_scripts','py.test-3.4'
__requires__ = 'pytest==2.5.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pytest==2.5.2', 'console_scripts', 'py.test-3.4')()
    )
