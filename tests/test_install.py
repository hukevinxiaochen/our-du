import subprocess

def test_command():
    """the command ourdu should run
    """
    our_du = ["our_du", "."]
    assert subprocess.call(our_du) == 0

