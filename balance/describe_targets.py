from jdcloud_sdk.services.lb.apis.DescribeTargetsRequest import DescribeTargetsParameters,DescribeTargetsRequest
from lbClient import *


def describeTargets():
    client = getLbClient()

    try:
        parameters = DescribeTargetsParameters("cn-north-1", "tg-hgphycy2lp")

        request = DescribeTargetsRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeTargets()
