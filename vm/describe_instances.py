from jdcloud_sdk.services.vm.apis.DescribeInstancesRequest import DescribeInstancesParameters, DescribeInstancesRequest
from vmClient import *


def describeInstances():
    client = getVmClient()

    try:
        parameters = DescribeInstancesParameters("cn-north-1")
        parameters.setPageSize(20)
        parameters.setPageNumber(1)

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
