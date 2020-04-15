from gevent import monkey;monkey.patch_all()

import subprocess

subprocess.call(["ls","-la"])

'''
As we have seen , in example-3.py we monkey patched socket interface.
In certain cases, we can't predict which method should be patch. 
Thus, monkey.patch_all method patches all class and methods implement to patch

It is always recommended that, to call monkey patch at start of any process, ie,
first line of your process to avoid unpredictable behavior and unexpected exitLoop
'''
