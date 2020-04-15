from gevent import monkey;monkey.patch_all()

import subprocess

subprocess.call(["ls","-la"])

'''
As we have seen , in example-3.py we monkey patched socket interface.
In certain cases, we can't predict which method should be patched.
Thus, monkey.patch_all() method patches all the methods of all classes.

It is recommended to call the monkey patch at start of the main process, ie,
first line of your process.
This is just to avoid unpredictable behavior and unexpected exitLoop.
'''
