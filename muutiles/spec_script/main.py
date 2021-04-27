import logging
import shutil
import os
import sys
a=['/home/weidong/Desktop/testcases/utiles/spec_script', '/home/weidong/Desktop/testcases', '/opt/apps/com.jetbrains.pycharm/plugins/python/helpers/pycharm_display', '/usr/lib/python37.zip', '/usr/lib/python3.7', '/usr/lib/python3.7/lib-dynload', '/home/weidong/.local/lib/python3.7/site-packages', '/usr/local/lib/python3.7/dist-packages', '/usr/lib/python3/dist-packages', '/opt/apps/com.jetbrains.pycharm/plugins/python/helpers/pycharm_matplotlib_backend']
for i in a:
    sys.path.append(i)
from  utiles.spec_script.merge_requires import MergeRequires
# logging.basicConfig(level=logging.DEBUG)
# os.remove('tt')
# shutil.copy('test.spec','tt')
# tmp=MergeRequires('tt')
# print(sys.path)
tmp=MergeRequires(sys.argv[1])
tmp.setup()