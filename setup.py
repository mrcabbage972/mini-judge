from setuptools import find_packages
from setuptools import setup

setup(
    name='mini_judge',
    description='Simple implementation of LLM-As-Judge',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Victor May',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={'': ['*.jsonl']},
    entry_points={'console_scripts': ['mini_judge=mini_judge.main:main']}
)
