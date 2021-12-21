from jdcloud_sdk.services.vpc.apis.DescribeElasticIpsRequest import DescribeElasticIpsParameters, \
    DescribeElasticIpsRequest
from vpcClient import *


def describeElasticIps():
    client = getVpcClient()
    try:
        parameter = DescribeElasticIpsParameters("cn-north-1")
        parameter.setPageNumber(1)
        parameter.setPageSize(10)
        request = DescribeElasticIpsRequest(parameter)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeElasticIps()
