"""DCOS Spark

Usage:
    dcos spark --help
    dcos spark --info
    dcos spark --version
    dcos spark run [<args>...]
    dcos spark status <submissionId>
    dcos spark kill <submissionId>

Options:
    --help                  Show this screen
    --info                  Show info
    --version               Show version
"""
import docopt
from dcos_spark import constants, dcos, spark_submit

master = "10.51.128.131:7077"

def run_spark_job(args):
    return spark_submit.submit_job(master, args['<args>'])

def job_status(args):
    return spark_submit.job_status(master, args['<submissionId>'])

def kill_job(args):
    return spark_submit.kill_job(master, args['<submissionId>'])

def main():
    args = docopt.docopt(
        __doc__,
        version='dcos-spark version {}'.format(constants.version),
        options_first=True)

    if args['--info']:
        print('Run and manage Spark jobs')
    elif args['run']:
        return run_spark_job(args)
    elif args['status']:
        return job_status(args)
    elif args['kill']:
        return kill_job(args)
    else:
        print(__doc__)
        return 1

    return 0
