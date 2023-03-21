from jdcloud_sdk.services.antipro.apis.DescribeInstanceRequest import DescribeInstanceParameters, DescribeInstanceRequest
from antipro_client import *


def describeInstance():
    client = getAntiproClient()
    try:
        parameters = DescribeInstanceParameters("cn-north-1", "")
        request = DescribeInstanceRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeInstance()
