#!/usr/bin/env python
"""Use My DU to keep your files clean.

SYSTEM REQUIREMENTS:
    - OS X 10.10.5
    - GNU coreutils installed via Homebrew
    - Python 3.5.1
"""

from sys import executable as which_python
print("Welcome. We are using the python located here {}".format(which_python))

import subprocess

# Use data from GNU coreutils' stat.
# We invoke it using the token `gstat` because OS X includes its own stat.

def stat(path_to_file):
    """stat invokes gstat

    gstat is invoked with the --format option:

    %s - size in bytes
    %x - last accessed date
    %w - birth date
    %n - file name

    TODO: Make this script work on Linux too.
    """

    completed_process = subprocess.run(["gstat", "--format", "%s %x %w %n", path_to_file], stdout=subprocess.PIPE)

    # print(completed_process.stdout)
    stats = completed_process.stdout
    return stats

if __name__ == "__main__":
    stat("README.markdown")
