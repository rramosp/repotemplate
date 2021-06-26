from setuptools import setup, find_packages, find_namespace_packages

setup(
    name = 'repotemplate',
    version = '0.1.0',
    package_dir = {"": "src"},
    packages = find_packages(where="src")
)