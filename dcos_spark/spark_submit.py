
"""
  This method runs spark_submit with the passed in parameters.
  ie: ./bin/spark-submit --deploy-mode cluster --class org.apache.spark.examples.SparkPi
      --master mesos://10.127.131.174:8077 --executor-memory 1G --total-executor-cores 100
     --driver-memory 1G http://10.127.131.174:8000/spark-examples_2.10-1.3.0-SNAPSHOT.jar 30
"""
def spark_submit(master, jar, appArgs, extraLibs, otherArgs, main_class = ""):
    return 0
