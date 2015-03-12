"""DCOS Spark Example Subcommand

Usage:
    dcos spark info

Options:
    --help           Show this screen
    --version        Show version
"""
import docopt
from dcos_spark import constants


def main():
    args = docopt.docopt(
        __doc__,
        version='dcos-marathon version {}'.format(constants.version))

    if args['spark'] and args['info']:
        print('Example of a DCOS subcommand')
    else:
        print(__doc__)
        return 1

    return 0
