from setuptools import setup

setup(
    name='our_du',
    version='0.1',
    py_modules=['our_du'],
    install_requires=[
        'Click',
        'pytest',
    ],
    entry_points='''
        [console_scripts]
        our_du=our_du:our_du
    ''',
)
