from setuptools import setup
from setuptools import find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pandavro-aa',
    version='1.9.0',
    description='Fork of ynqa/pandavro to support newer numpy releases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fredcohen-aa/pandavro',
    author='Fred Cohen',
    author_email='fred.cohen@aa.com',
    license='MIT',
    packages=find_packages(exclude=['example']),
    install_requires=[
        # fixed versions.
        'fastavro>=1.5.1,<2.0.0',
        'pandas>=2.0,<3.0.0',
        'numpy>=2.0,<3.0.0',
    ],
    extras_require={
        'tests': ['pytest==7.3.2', 'tox==4.6.0'],
    },
    # https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/install.html#python-version-support
    python_requires='>=3.9.0',
)
