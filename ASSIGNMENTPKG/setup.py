from setuptools import setup, find_packages

setup(
    name='assignmentpkg',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'spotipy',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'assignmentpkg =
