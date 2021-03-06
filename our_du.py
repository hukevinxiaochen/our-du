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
IGNORE_THESE = [".git", \
        ".gitignore",   \
        "bin",          \
        "usr",          \
        ".cache",       \
        "venv",         \
        "__pycache__",  \
        "our_du.egg-info"]

# Define some helpers
from os import path
def should_ignore(file_name):
    """Removes files that we want to ignore from walk path
    """
    if file_name in IGNORE_THESE:
        return True
    else:
        return False

def getfiledata(file_path):
    """Gets data about file at file_path

    path.getatime - returns last access time

    Returns a tuple with relevant data.
    """
    last_access_time_since_epoch = path.getatime(file_path)

    size = path.getsize(file_path)
    return last_access_time_since_epoch, size, file_path

from time import ctime
def stringify(stat):
    """Converts sequence of projects to output string.

    stat is a tuple:

    last_access_time_since_epoch - float,
    size - in Bytes, string or float, I dunno,
    file_path - string I think, absolute
    """
    last_access_time_since_epoch, size, file_path = stat
    last_access_time = ctime(last_access_time_since_epoch)
    return "{}\t{}\t{}\n".format(last_access_time, size, file_path)

# Begin the command line interface
from os import walk
from operator import itemgetter

# Note the click.File('w') pattern. See <https://youtu.be/kNke39OZ2k0>
# defaults to stdout, which is apparently represented by a dash
@click.command()
@click.argument('f')
@click.option('--o', type=click.File('w'), default='/dev/stdout')
def our_du(f, o):
    """Walks the file hierarchy for folder f.

    os.walk visits all the directories and files inside of folder f.
    It does so recursively, meaning it then visits all the directories
    and files inside of any directories it encounters in a given pass.
    With each pass, it makes available for use a tuple of the following:

    fpath - the path of folder f
    fsbdrn - a list of names of subdirectories found in folder f
    ffilesn - a list of names of files found in folder f

    IGNORE_THESE - a global, see above. It lists all the files we do not
    actually care to examine/check.

    getfiledata - returns a tuple with last_access_time, size, file_path
    """
    everything = []
    for frootp, fsbdrn, ffilesn in walk(f):
        # ignore files found in IGNORE_THESE
        fsbdrn[:] = [x for x in fsbdrn if not should_ignore(x)]
        ffilesn[:] = [x for x in ffilesn if not should_ignore(x)]
        # bring together all the directories and files for data collection
        all_the_stuff = fsbdrn + ffilesn
        # form relative path from names and convert to absolute paths
        all_the_stuff[:] = [path.abspath(path.join(frootp, x)) for x in \
                all_the_stuff]
        stats = [getfiledata(x) for x in all_the_stuff]
        everything += stats

    everything[:] = sorted(everything, key=itemgetter(0))
    everything[:] = sorted(everything, key=itemgetter(1), reverse=True)

    for stat in everything:
        stat_str = stringify(stat)
        o.write(stat_str)

