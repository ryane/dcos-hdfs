from common import exec_command


def test_help():
    returncode, stdout, stderr = exec_command(
        ['dcos-hdfs', 'hdfs', '--help'])

    assert returncode == 0
    assert stderr == b''
