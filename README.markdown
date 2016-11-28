# Motivation

This script is the beginning of a more responsible approach to using precious SSD space. It aims to make staying neat and space-efficient easy by showing users the directories that are actively used versus stale versus ready for archiving.

# How it works

## Python Subprocess

The Python [subprocess][subprocess] library as proposed in [PEP](https://www.python.org/dev/peps/pep-0324/) is a great way to make Python a replacement language for over-complicated shell scripts.

One of the main ways to gain insight about disk usage is the GNU coreutil [du][du].

With [subprocess][subprocess], we can take the output of [du][du] and manipulate with Python.

