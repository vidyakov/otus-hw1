import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


setup(
    name='search_tool',
    version='0.1',
    packages=['search_engine'],
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='Genereates random number',
    long_description=README,
    author='vidyakov',
    entry_points={
        'console_scripts': [
            'search = search_engine.main',
        ]
    },
)
