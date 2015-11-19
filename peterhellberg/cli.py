'''
Command-line runner for peterhellberg
'''

import argparse
import requests
from . import main, metadata


def parse_args():
    '''Argument Parser.'''
    parser = argparse.ArgumentParser(
        description=metadata.__description__,
        epilog="see {0} for source code, feature requests and bug reports".format(metadata.__repo__)
    )

    parser.add_argument('url',
                        metavar='URL', nargs=1,
                        help='URL of the site')

    parser.add_argument('-s', '--ssl',
                        action='store_true',
                        help='use SSL')

    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s {0}'.format(metadata.__version__))

    args = parser.parse_args()
    args = vars(args)
    return args


def run():
    args = parse_args()
    try:
        res = main.parse(args['url'][0], use_ssl=args['ssl'])
        print(res)
    except requests.exceptions.RequestException as exception:
        main.diagnose(exception)
        exit(1)


if __name__ == '__main__':
    run()

