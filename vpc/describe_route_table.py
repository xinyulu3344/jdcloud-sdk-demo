#!/usr/bin/python3
from jdcloud_sdk.services.vpc.apis.DescribeRouteTableRequest import DescribeRouteTableParameters, \
    DescribeRouteTableRequest
from vpcClient import *


def describeRouteTable():
    client = getVpcClient()
    try:
        parameters = DescribeRouteTableParameters("cn-north-1", "rtb-faf0pcrx62")
        request = DescribeRouteTableRequest(parameters)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeRouteTable()
