from setuptools import setup, find_packages
from os import path

setup(
    name='smpl',  # Required
    version='0.1',  # Required
    description='A simple Sphinx theme.',
    url='https://github.com/simonpf/smpl',  # Optional
    author='Simon Pfreundschuh',  # Optional
    author_email='simon.pfreundschuh@chalmers.se',  # Optional
    packages=["smpl"],
    python_requires='>=3.6',
    entry_points = {
            'sphinx.html_themes': [
                'smpl = smpl',
            ]
        },
    project_urls={  # Optional
        'Source': 'https://github.com/simonpf/smpl/',
    })
