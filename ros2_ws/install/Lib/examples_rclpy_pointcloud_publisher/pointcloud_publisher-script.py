#!c:\python38\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'examples-rclpy-pointcloud-publisher==0.17.1','console_scripts','pointcloud_publisher'
__requires__ = 'examples-rclpy-pointcloud-publisher==0.17.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('examples-rclpy-pointcloud-publisher==0.17.1', 'console_scripts', 'pointcloud_publisher')()
    )
