""" This is a simple Python library for interacting with the REST interface of an instance of Cordra.
"""

from setuptools import setup

def fetch_requirements():
    required = []
    with open('requirements.txt') as f:
        required = f.read().splitlines()
    return required

setup(
    name="cordra",
    py_modules=['cordra'],
    version='0.3',
    description='Python client interface to a cordra instance',
    Long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    author='Zachary Trautt, Faical Yannick Congo',
    author_email='zachary.trautt@nist.gov',
    include_package_data=True,
    install_requires=fetch_requirements()
)

# Set up using this video: https://www.youtube.com/watch?v=zhpI6Yhz9_4