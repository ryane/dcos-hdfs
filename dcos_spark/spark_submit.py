from dcos_spark import constants
import pkg_resources

"""
  This method runs spark_submit with the passed in parameters.
  ie: ./bin/spark-submit --deploy-mode cluster --class org.apache.spark.examples.SparkPi
      --master mesos://10.127.131.174:8077 --executor-memory 1G --total-executor-cores 100
     --driver-memory 1G http://10.127.131.174:8000/spark-examples_2.10-1.3.0-SNAPSHOT.jar 30
"""
def run(master, jar, options):
    submit_file = pkg_resources.resource_filename(
        'dcos_spark',
        'data/' + constants.spark_version + '/bin/spark-submit.sh')

    command = submit_file + " --deploy-mode cluster --master mesos://" + master + " " + options

    process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    return process.returncode
