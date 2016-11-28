#!/usr/bin/env python
"""
SYSTEM REQUIREMENTS:
    - OS X 10.10.5
    - GNU coreutils installed via Homebrew
    - Python 3.5.1
"""

from sys import executable as which_python
print("Welcome. We are using the python located here {}".format(which_python))

import subprocess

# Use data from stat
# The process we are calling is gstat because this script assumes
completed_process = subprocess.run(["ls", "-al"], stdout=subprocess.PIPE)
print(completed_process.stdout)

