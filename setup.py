import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ThreadedCommand',
    version='0.1',
    packages=['threadedcommand'],
    author="Mike Bertram",
    author_email="contact@mibexx.de",
    description="Runs a console command in multiple threads",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mibexx/threaded_command",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
