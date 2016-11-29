"""Use Our DU to manage our disk space.

SYSTEM REQUIREMENTS:
    - OS X 10.10.5
    - Python 3.5.1
"""
# Use the Click framework. Pocoo is incredible. Long live Armin Ronacher!
import click

# Some useful administrative information
from sys import executable as which_python

def about():
    """Print some runtime details.
    """
    print("Welcome. We are using the python located here {}.".format(which_python))

# Useful reference information
IGNORE_THESE = [".git", ".gitignore", "bin", "usr", ".cache", "venv", "__pycache__", "our_du.egg-info"]

# Define some helpers
from os import path

def getfiledata(p):
    """Gets data about file at path p

    Returns a formatted string with relevant data.
    """
    last_access_time = path.getatime(p)
    size = path.getsize(p)
    return "{}\t{}\t{}".format(last_access_time, size, p)

def should_ignore(x):
    """Removes files that we want to ignore from walk path
    """
    if x in IGNORE_THESE:
        return True
    else:
        return False

# Let's get down to business
from os import walk, stat
import pprint
from itertools import filterfalse

@click.command()
@click.argument('f')
def our_du(f):
    """Walks the file hierarchy for folder f.

    fpath - the path of folder f
    fsbdrn - a list of names of subdirectories found in folder f
    ffilesn - a list of names of files found in folder f

    IGNORE_THESE - a global, see above. It lists all the files we do not
    actually care to examine/check.
    """
    for frootp, fsbdrn, ffilesn in walk(f):
        pp = pprint.PrettyPrinter(indent=4)

        print("Initial directory list")
        pp.pprint(fsbdrn)
        fsbdrn[:] = [x for x in fsbdrn if not should_ignore(x)]
        # removeignorednames(fsbdrn)
        print("Filtered directory list")
        pp.pprint(fsbdrn)
        ffilesn[:] = [x for x in ffilesn if not should_ignore(x)]
        # removeignorednames(ffilesn)
 
        all_the_stuff = fsbdrn + ffilesn

        all_the_paths = [path.abspath(path.join(frootp, x)) for x in \
                all_the_stuff]
        stats = [getfiledata(x) for x in all_the_paths]
        # pp.pprint(stats)

