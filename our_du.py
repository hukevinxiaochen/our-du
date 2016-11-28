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

# Let's get down to business
import subprocess

# TODO: Consider using decorators to abstract these GNU utils
# A function that takes file arguments and spits out the desired info.
def stat(file_path):
    """Invokes GNU stat (gstat on OS X)

    gstat is what we call the GNU coreutils `stat` package when we are on OS X.

    gstat is invoked with the --format option:

    %s - size in bytes
    %x - last accessed date
    %w - birth date
    %n - file name

    TODO: Make this script work on Linux too.
    """

    completed_process = subprocess.run(["gstat", "--format", "%s %x %w %n", file_path], stdout=subprocess.PIPE)

    # print(completed_process.stdout)
    stats = completed_process.stdout
    return stats

def find(file_path):
    """Invokes GNU find (gfind on OS X)
    """

    completed_process = subprocess.run(["gfind", file_path, "-printf", "%a %s %p"], stdout=subprocess.PIPE)

    # print(completed_process.stdout)
    found = completed_process.stdout
    return found

if __name__ == "__main__":
    stat("README.markdown")

