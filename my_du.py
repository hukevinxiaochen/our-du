#!/usr/bin/env python
from sys import executable as which_python
print("Welcome. We are using the python located here {}".format(which_python))

import subprocess

# Use du
completed_process = subprocess.run(["ls", "-al"], stdout=subprocess.PIPE)
print(completed_process.stdout)

