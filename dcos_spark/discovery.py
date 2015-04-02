import json
import toml
import requests
import os
import sys

def get_spark_dispatcher():
    dcos_config = os.getenv("DCOS_CONFIG")
    if dcos_config is None:
        print("Please specify DCOS_CONFIG env variable for reading DCOS config")
        sys.exit(1)

    with open(dcos_config) as f:
      config = toml.loads(f.read())

    marathon = config["marathon"]
    url = "http://" + marathon["host"] + ":" + str(marathon["port"]) + "/v2/apps/spark"

    response = requests.get(url, timeout=5)

    if response.status_code >= 200:
        if 'app' not in response.json():
            print response.json()['message']
            sys.exit(1)

        tasks = response.json()['app']['tasks']

        if len(tasks) == 0:
            print "Spark cluster task is not running yet."
            sys.exit(1)

        spark_task = tasks[0]

        if len(spark_task["ports"]) == 0:
            print "No port found from the running task."
            sys.exit(1)

        return "mesos://" + spark_task["host"] + ":" + str(spark_task["ports"][0])
    else:
        print "Bad response getting marathon app def. Status code: " + str(response.status_code)
        sys.exit(1)
        return ""
