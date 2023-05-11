from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Script for sorting files in folder',
    url='https://github.com/takeRednotBlue/Python-core/tree/main-chgd/hw7/HW_project/clean_folder/clean_folder',
    author='Maksym Klym',
    author_email='maxymklym1996@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts':[
            'clean-folder = clean_folder.main:main'
        ]
    }
)