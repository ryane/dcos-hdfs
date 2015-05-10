"""Utilities for building and managing your HDFS installation

Usage:
    dcos hdfs --help
    dcos hdfs --info
    dcos hdfs --version
    dcos hdfs config-gen <filename>

Commands:
    config-gen: This subcommand allows you to create a configuration file
                to pass into a DCOS package install command for HDFS. Please
                copy and configure your own mesos-site.xml file and pass it
                into config-gen to generate your own 'options.json' file.
                Then you may install your customized version of HDFS with
                'dcos package install --options=./options.json hdfs'
Options:
    --help                  Show this screen
    --info                  Show info
    --version               Show version
"""
import base64
import docopt
import json
import os
import sys

from dcos_hdfs import constants


def gen_config(args):
    filename = args['<filename>']
    if not os.path.isfile(filename):
        print("Cannot find file " + filename)
        return 1

    with open (filename, "r") as config_file:
        data = config_file.read().encode('ascii')

    config = {}
    config[constants.custom_config_key] = base64.b64encode(data).decode('utf-8')

    with open('options.json', 'w') as config_output:
        json.dump(config, config_output,
            sort_keys=True, indent=4, separators=(',', ': '))

    return 0


def main():
    args = docopt.docopt(
        __doc__,
        version='dcos-hdfs version {}'.format(constants.version), help=False)

    if args['--info']:
        print(__doc__.split('\n')[0])
    elif args['config-gen']:
        return gen_config(args)
    else:
        print(__doc__)
        return 1

    return 0
