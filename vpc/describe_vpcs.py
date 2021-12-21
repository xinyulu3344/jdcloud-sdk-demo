from jdcloud_sdk.services.vpc.apis.DescribeVpcsRequest import DescribeVpcsParameters, DescribeVpcsRequest
from vpcClient import *


def describeVpcs():
    client = getVpcClient()
    try:
        parameters = DescribeVpcsParameters("cn-south-1")
        parameters.setPageNumber(1)
        parameters.setPageSize(100)

        request = DescribeVpcsRequest(parameters)
        resp = client.send(request)

        print("requestId: ", resp.request_id)
        # 错误处理
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return

        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeVpcs()
