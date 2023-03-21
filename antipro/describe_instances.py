from jdcloud_sdk.services.antipro.apis.DescribeInstancesRequest import DescribeInstancesParameters, DescribeInstancesRequest
from antipro_client import *


def describeInstances():
    client = getAntiproClient()
    try:
        parameters = DescribeInstancesParameters("cn-north-1")
        request = DescribeInstancesRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeInstances()
