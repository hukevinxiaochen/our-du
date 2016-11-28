# Motivation

This script is the beginning of a more responsible approach to using precious SSD space. It aims to make staying neat and space-efficient easy by showing users the directories that are actively used versus stale versus ready for archiving.

## Conservation

One of the principles of responsible resource management is conservation. The greenest building is the one that is never built. Similarly, disk space is something that should be conserved (I think).

# How it works

## Python Subprocess

The Python [subprocess][subprocess] library as proposed in [PEP](https://www.python.org/dev/peps/pep-0324/) is a great way to make Python a replacement language for over-complicated shell scripts.

One of the main ways to gain insight about disk usage is the GNU coreutil [du][du].

With [subprocess][subprocess], we can take the output of [du][du] and manipulate it with Python.

## GNU coreutils

This script relies heavily on GNU coreutils. In essence, we are trying to a reasonable front-end to core system tools that will help us efficiently manage disk space.

[stat][stat] can return the birth date, most recent access date, and the file size of any file.

[du][du] can return file sizes for all files within a file hierarchy.

[fts][fts] helps us traverse the file hierarchy.

# Contribute

## Get dependencies

Set up a virtual environment using `python -m venv virtual_env`.

## Test

Run tests using `py.test`. I suck at testing so I just chose something off-the-shelf.


