#!/Users/KHU/Desktop/keep/tools/our_du/virtual_env/bin/python
"""Use Our DU to manage our disk space.

SYSTEM REQUIREMENTS:
    - OS X 10.10.5
    - Python 3.5.1
"""

# Some useful administrative information
from sys import executable as which_python

def about():
    """Print some runtime details.
    """
    print("Welcome. We are using the python located here {}.".format(which_python))

# Useful reference information
IGNORE_THESE = [".git", ".gitignore", "bin", "usr", ".cache", "virtual_env"]

# Define some helpers
from os import path

def getfiledata(p):
    """Gets data about file at path p

    Returns a formatted string with relevant data.
    """
    last_access_time = path.getatime(p)
    size = path.getsize(p)
    return "{}\t{}\t{}".format(last_access_time, size, p)

def removeignorednames(l):
    """Removes files that we want to ignore from walk path
    """
    for x in l:
        if x in IGNORE_THESE:
            l.remove(x)

# Let's get down to business
from os import walk, stat
import pprint

def our_du(f):
    """Walks the file hierarchy for folder f.

    fpath - the path of folder f
    fsbdrn - a list of names of subdirectories found in folder f
    ffilesn - a list of names of files found in folder f

    IGNORE_THESE - a global, see above. It lists all the files we do not
    actually care to examine/check.
    """
    for frootp, fsbdrn, ffilesn in walk(f):
        removeignorednames(fsbdrn)
        removeignorednames(ffilesn)
        all_the_stuff = fsbdrn + ffilesn
        
        pp = pprint.PrettyPrinter(indent=4)
        
        all_the_paths = [path.abspath(path.join(frootp, x)) for x in \
                all_the_stuff]
        stats = [getfiledata(x) for x in all_the_paths]
        pp.pprint(stats)

if __name__ == "__main__":
    about()
    our_du(".")

