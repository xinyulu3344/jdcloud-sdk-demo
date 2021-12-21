from jdcloud_sdk.services.rds.apis.DescribeSlowLogAttributesRequest import DescribeSlowLogAttributesParameters, \
    DescribeSlowLogAttributesRequest
from rdsClient import *


def describeSlowLogAttributes():
    client = getRdsClient()

    try:
        parameters = DescribeSlowLogAttributesParameters("cn-north-1", "mysql-ykdunggylk", "2021-12-20 12:00:00", "2021-12-21 12:00:00")

        request = DescribeSlowLogAttributesRequest(parameters)
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
    describeSlowLogAttributes()
