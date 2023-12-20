from setuptools import setup, find_packages

setup(
    name="webscrapper_proto",
    version="0.1",
    packages=find_packages(include=['gen*', 'gen.python*', 'gen.python.scrapper*']),
)