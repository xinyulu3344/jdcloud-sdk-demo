from jdcloud_sdk.services.vpc.apis.DescribeNetworkInterfacesRequest import DescribeNetworkInterfacesParameters, \
    DescribeNetworkInterfacesRequest
from vpcClient import *


def describeNetworkInterfaces():
    client = getVpcClient()
    try:
        parameter = DescribeNetworkInterfacesParameters("cn-north-1")
        parameter.setPageSize(100)
        request = DescribeNetworkInterfacesRequest(parameter)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeNetworkInterfaces()
