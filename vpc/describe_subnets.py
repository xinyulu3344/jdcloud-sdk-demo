from jdcloud_sdk.services.vpc.apis.DescribeSubnetsRequest import DescribeSubnetsParameters, DescribeSubnetsRequest
from vpcClient import *


def describeSubnets():
    client = getVpcClient()
    try:
        parameter = DescribeSubnetsParameters("cn-north-1")
        request = DescribeSubnetsRequest(parameter)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        result = resp.result
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeSubnets()
