from jdcloud_sdk.services.vm.apis.DescribeInstanceRequest import DescribeInstanceParameters, DescribeInstanceRequest
from vmClient import *


def describeInstance(regionId, instanceId):
    client = getVmClient()

    try:
        parameters = DescribeInstanceParameters(regionId, instanceId)
        request = DescribeInstanceRequest(parameters)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeInstance("cn-north-1", "i-vw11z002j8")
