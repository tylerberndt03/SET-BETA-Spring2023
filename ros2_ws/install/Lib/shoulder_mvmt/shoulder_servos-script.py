#!c:\python38\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'shoulder-mvmt==0.0.0','console_scripts','shoulder_servos'
__requires__ = 'shoulder-mvmt==0.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('shoulder-mvmt==0.0.0', 'console_scripts', 'shoulder_servos')()
    )
