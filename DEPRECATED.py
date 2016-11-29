"""DEPRECATED:
    - stat | discovery
    - find | discovery
"""

import subprocess
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


