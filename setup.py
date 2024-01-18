from setuptools import setup

setup(
    name='hello_world',
    version='1.0',
    py_modules=['hello_world'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        cli=hello_world:cli
'''
)