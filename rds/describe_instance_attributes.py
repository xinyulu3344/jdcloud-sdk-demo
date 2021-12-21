from jdcloud_sdk.services.rds.apis.DescribeInstanceAttributesRequest import DescribeInstanceAttributesParameters, \
    DescribeInstanceAttributesRequest
from rdsClient import *


def describeInstanceAttributes():
    client = getRdsClient()

    try:
        parameters = DescribeInstanceAttributesParameters("cn-north-1", "mysql-ykdunggylk")
        request = DescribeInstanceAttributesRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        result = resp.result
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeInstanceAttributes()
