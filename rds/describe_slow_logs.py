from jdcloud_sdk.services.rds.apis.DescribeSlowLogsRequest import DescribeSlowLogsParameters, DescribeSlowLogsRequest
from rdsClient import *


def describeSlowLogs():
    client = getRdsClient()

    try:
        parameters = DescribeSlowLogsParameters("cn-north-1", "mysql-f1w4ledggm", "2019-12-16 00:00:00", "2019-12-16 02:00:00")

        request = DescribeSlowLogsRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeSlowLogs()
