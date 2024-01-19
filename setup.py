from setuptools import setup

setup(
    name='naval',
    version='1.0',
    py_modules=['hello_world','restaurant','inout','naval'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        say=hello_world:say
        food=restaurant:freddys
        inout=inout:cli
        naval=naval:cli
'''
)