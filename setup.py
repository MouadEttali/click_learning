from setuptools import setup

setup(
    name='aliases',
    version='1.0',
    py_modules=['hello_world','restaurant','inout','naval',"aliases",'colors','termui'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        say=hello_world:say
        food=restaurant:freddys
        inout=inout:cli
        naval=naval:cli
        aliases=aliases:cli
        colors=colors:cli
        termui=termui:cli

'''
)