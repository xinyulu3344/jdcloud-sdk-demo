from jdcloud_sdk.services.kafka.apis.DescribeInstanceRequest import DescribeInstanceParameters, DescribeInstanceRequest
from kafkaClient import *


def describeInstance():
    client = getKafkaClient()
    try:
        parameters = DescribeInstanceParameters("cn-north-1", "kafka-crm6gp77ia")
        request = DescribeInstanceRequest(parameters)
        resp = client.send(request)
        print("requestId: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeInstance()
