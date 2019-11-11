from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="arrange-honeycomb",
    version="0.0.1",
    author="Tyler Cone",
    author_email="herrflockig@gmail.com",
    description="A command line tool to arrange icons for the Honeycomb plugin for Rainmeter.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/arrange-honeycomb/arrange-honeycomb/",
    packages=find_packages(),
    install_requires=['hexy'],
    entry_points={
        'console_scripts': [
            'arrange-honeycomb = arrangehoneycomb.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
)