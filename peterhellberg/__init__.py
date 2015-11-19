'''
peterhellberg
~~~~~~~~~~~~~
A module for interacting with PeterHellBerg's
web application, for parsing humans.txt into JSON. The app is
exposed at http://humans.herokuapp.com/.
'''

from .metadata import __description__, __version__, __license__
from .cli import run
from .main import parse, diagnose


__all__ = ['__description__', '__version__', '__license__', 'parse', 'diagnose', 'run', ]
