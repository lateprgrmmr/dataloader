from setuptools import setup

setup(
    name='names',
    version='0.1',
    py_modules=['names'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        names=names:cli
    ''',
)