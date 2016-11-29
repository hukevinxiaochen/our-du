import subprocess

WHERE_SHIT_BE_AT = "/Users/KHU/Desktop/keep/tools/our_du"
SCRIPT_NAME = "our_du.py"

def test_it_is_executable():
    path_to_script = "{0}/{1}".format(WHERE_SHIT_BE_AT, SCRIPT_NAME)
    assert subprocess.call([path_to_script]) == 0

