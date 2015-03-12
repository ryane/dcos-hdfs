from common import exec_command


def test_help():
    returncode, stdout, stderr = exec_command(
        ['dcos-spark', 'spark', '--help'])

    assert returncode == 0
    assert stdout == b"""DCOS Spark Example Subcommand

Usage:
    dcos spark info

Options:
    --help           Show this screen
    --version        Show version
"""
    assert stderr == b''
