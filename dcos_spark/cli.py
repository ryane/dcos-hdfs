"""DCOS Spark

Usage:
    dcos spark --help
    dcos spark --info
    dcos spark --version
    dcos spark run <jarUrl> [<args>...]

Options:
    --help                  Show this screen
    --info                  Show info
    --version               Show version
"""
import docopt
from dcos_spark import constants, dcos, spark_submit

def run_spark_job(args):
    spark_submit.run("master", args['<jarUrl>'], args['<args>'])
    return 0

def main():
    args = docopt.docopt(
        __doc__,
        version='dcos-spark version {}'.format(constants.version))

    if args['--info']:
        print('Run and manage Spark jobs')
    elif args['run']:
        return run_spark_job(args)
    else:
        print(__doc__)
        return 1

    return 0
