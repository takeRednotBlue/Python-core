from setuptools import setup, find_namespace_packages

setup(
    name="cli-bot",
    version='0.0.1',
    description='Command line assistant bot.',
    author='Maksym Klym',
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts':[
            'start-bot = src.main:main'
        ]
    }
)