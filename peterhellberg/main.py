'''
The Core of peterhellberg
'''

import requests
from . import metadata


def parse(url, use_ssl=False):
    '''Send a http request to the remote server

    Return the response, as a dictionary
    Raises requests.exceptions.ConnectionError in event of a network error
    Raises requests.exceptions.HTTPError in event of invalid HTTP response
    Raises requests.exceptions.Timeout in event of a request timeout
    Raises requests.exceptions.TooManyRedirects in event of too many redirects'''
    params = {}
    params['use_ssl'] = use_ssl
    res = requests.get('{0}/{1}'.format(metadata.APP_URL, url), params=params)
    res.raise_for_status()
    return res.json()


def diagnose(exception):
    '''Diagnose issues. Useful when errors occur.'''
    if isinstance(exception, requests.exceptions.ConnectionError):
        print("error: network error")
    elif isinstance(exception, requests.exceptions.HTTPError):
        print("error: invalid HTTP response")
    elif isinstance(exception, requests.exceptions.Timeout):
        print("error: request timeout")
    elif isinstance(exception, requests.exceptions.TooManyRedirects):
        print("error: too many redirects")
    else:
        print("error: unknown exception")
        print exception
