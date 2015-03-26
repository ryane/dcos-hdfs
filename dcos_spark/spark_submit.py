from dcos_spark import constants
import pkg_resources
import subprocess
import json

def submit_job(master, args):
    response = run(master, args)
    if response[0] != None:
        print "Run job succeeded. Submission id: " + response[0]['submissionId']
    return response[1]

def job_status(master, submissionId):
    response = run(master, ["--status", submissionId])
    if response[0] != None:
        print "Submission ID: " + response[0]['submissionId']
        print "Driver state: " + response[0]['driverState']
        print "Last status: " + response[0]['message']
    return response[1]

def kill_job(master, submissionId):
    response = run(master, ["--kill", submissionId])
    if response[0] != None:
        if bool(response[0]['success']):
            success = "succeeded."
        else:
            success = "failed."
        print "Kill job " + success
        print "Message: " + response[0]['message']
    return response[1]

"""
  This method runs spark_submit with the passed in parameters.
  ie: ./bin/spark-submit --deploy-mode cluster --class org.apache.spark.examples.SparkPi
      --master mesos://10.127.131.174:8077 --executor-memory 1G --total-executor-cores 100
     --driver-memory 1G http://10.127.131.174:8000/spark-examples_2.10-1.3.0-SNAPSHOT.jar 30
"""
def run(master, args):
    submit_file = pkg_resources.resource_filename(
        'dcos_spark',
        'data/' + constants.spark_version + '/bin/spark-submit')

    command = [submit_file, "--deploy-mode", "cluster", "--master", "mesos://" + master] + args

    process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print "Spark submit failed:"
        print stderr
        return (None, process.returncode)
    else:
        response = json.loads(stderr[stderr.index('{')::])
        return (response, process.returncode)
