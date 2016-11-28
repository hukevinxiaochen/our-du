#!/Users/KHU/Desktop/keep/tools/our_du/virtual_env/bin/python
"""Use Our DU to manage our disk space.

SYSTEM REQUIREMENTS:
    - OS X 10.10.5
    - GNU coreutils installed via Homebrew
    - Python 3.5.1
"""

# Some useful administrative information
from sys import executable as which_python
print("Welcome. We are using the python located here {}.".format(which_python))

import subprocess

def stat(path_to_file):
    """stat invokes gstat

    gstat is what we call the GNU coreutils `stat` package when we are on OS X.

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

