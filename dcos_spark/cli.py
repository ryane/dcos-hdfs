"""Run and manage Spark jobs

Usage:
    dcos spark --help
    dcos spark --info
    dcos spark --version
    dcos spark run --submit-args=<spark-args>
    dcos spark status <submissionId>
    dcos spark kill <submissionId>
    dcos spark webui

Options:
    --help                  Show this screen
    --info                  Show info
    --version               Show version
"""
import docopt
from dcos_spark import constants, discovery, spark_submit


def master():
    return discovery.get_spark_dispatcher()


def run_spark_job(args):
    return spark_submit.submit_job(master(), args['--submit-args'])


def job_status(args):
    return spark_submit.job_status(master(), args['<submissionId>'])


def kill_job(args):
    return spark_submit.kill_job(master(), args['<submissionId>'])


def print_webui(args):
    print discovery.get_spark_webui()
    return 0


def main():
    args = docopt.docopt(
        __doc__,
        version='dcos-spark version {}'.format(constants.version))

    if args['--info']:
        print(__doc__.split('\n')[0])
    elif args['run']:
        return run_spark_job(args)
    elif args['status']:
        return job_status(args)
    elif args['kill']:
        return kill_job(args)
    elif args['webui']:
        return print_webui(args)
    else:
        print(__doc__)
        return 1

    return 0
