'''
Setup script for peterhellberg
'''

from setuptools import setup
import peterhellberg


def get_requirements():
    '''Return a list of requirements for installation as listed in the
    requirements.txt file'''
    with open("requirements.txt", "r") as reqsFile:
        reqs = reqsFile.read()
        return reqs.strip().split("\n")


setup(
    name="peterhellberg",
    version=peterhellberg.__version__,
    author="GochoMugo",
    author_email="mugo@forfuture.co.ke",
    author_url="https://gochomugo.github.io/",
    url="https://github.com/forfuturellc/peterhellberg",
    download_url="https://github.com/forfuturellc/peterhellberg/zipball/master",
    description=peterhellberg.__description__,
    keywords=["humans.txt"],
    license="MIT",
    long_description=peterhellberg.__doc__,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4"
    ],
    packages=["peterhellberg"],
    install_requires=get_requirements(),
    entry_points={
        'console_scripts': [
            'get-humans = peterhellberg.cli:run',
        ]
    }
)

