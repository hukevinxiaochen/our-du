# I. Goals

* portability - write as a command line tool

# II. Motivation

This script is the beginning of a more responsible approach to using precious SSD space. It aims to make staying neat and space-efficient easy by showing users the directories that are actively used versus stale versus ready for archiving.

## A. Conservation

One of the principles of responsible resource management is conservation. The greenest building is the one that is never built. Similarly, disk space is something that should be conserved (I think).

# III. Getting Started

* TODO: Make this even easier. This is not very user friendly installation. Not user friendly usage either.
* TODO: Go to PyPA to learn how to package this up for PyPI, see sample repo and slack-cleaner for inspiration

clone the repo: `git clone`  
create a virtual environment `python -m venv venv`  
activate it `. venv/bin/activate`  
install the module into it `pip install --editable`  
run the tests `pytest tests`  
run it `our_du .`

# III. Contribute

## A. Get dependencies

Set up a virtual environment using `python -m venv virtual_env`. Make sure to have `wheel` installed per the [Python Packaging Authority][PyPA] - not sure why.

Get required python package dependencies using `pip install -r requirements.txt`.

## B. Install
We use setuptools develop mode. `pip install --editable .` This workflow involves installing our module into the local virtualenv.

### 1. Python packages

* pytest - testing framework

## B. Test

I activate the virtual environment to run tests using `pytest tests -v`. I suck at testing so I just chose something off-the-shelf.

# IV. Discovery 

In the early discovery stages of the project I wrote wrappers around GNU stat and GNU find, and did quite a bit of learning about those command line tools/how to use them to get file size and access time data.

If you are interested for academic purposes you can see how things looked then:

`git checkout -b discover discovery`

## A. Python Subprocess

The Python [subprocess][subprocess] library as proposed in [PEP](https://www.python.org/dev/peps/pep-0324/) is a great way to make Python a replacement language for over-complicated shell scripts.

One of the main ways to gain insight about disk usage is the GNU coreutil [du][du].

With [subprocess][subprocess], we can take the output of [du][du] and manipulate it with Python.

## B. GNU coreutils

This script relies heavily on GNU coreutils. In essence, we are trying to a reasonable front-end to core system tools that will help us efficiently manage disk space.

[stat][stat] can return the birth date, most recent access date, and the file size of any file.

[du][du] can return file sizes for all files within a file hierarchy.

[fts][fts] helps us traverse the file hierarchy.

[find][find] traverses the file hierachy while running [stat][stat] along the way. It provides options for filtering the file hierarchy as you go so you can find what you are interested in. It is part of the GNU [findutils][findutils].

