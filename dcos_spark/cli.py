"""DCOS Spark Example Subcommand

Usage:
    dcos spark info

Options:
    --help           Show this screen
    --info           Show info
    --version        Show version
"""
import docopt
from dcos_spark import constants, spark_submit


def run_spark_job(args):
    # How do I get the marathon uri, and dispatcher endpoint?
    return 0

def main():
    args = docopt.docopt(
        __doc__,
        version='dcos-spark version {}'.format(constants.version))

    if args['spark'] and args['info']:
        print('Run and manage Spark jobs')
    elif args['spark'] and args['run']:
        return run_spark_job(args)
    else:
        print(__doc__)
        return 1

    return 0
