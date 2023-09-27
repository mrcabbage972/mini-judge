from setuptools import find_packages
from setuptools import setup

setup(
    name='mini_judge',
    description='Simple implementation of LLM-As-Judge',
    author='Victor May',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
)
