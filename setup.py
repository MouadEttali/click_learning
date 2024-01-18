from setuptools import setup

setup(
    name='hello_world',
    version='1.0',
    py_modules=['hello_world','restaurant'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        hello=hello_world:say
        food=restaurant:freddys
        inout=inout:cli
'''
)