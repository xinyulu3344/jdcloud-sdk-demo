from jdcloud_sdk.services.rds.apis.DescribeLogsRequest import DescribeLogsParameters,DescribeLogsRequest
from jdcloud_sdk.services.common.models.Filter import Filter
from rdsClient import *


def describeLogs():
    client = getRdsClient()

    try:
        parameters = DescribeLogsParameters("cn-north-1", "mysql-ykdunggylk")
        filter1 = Filter(name="logType", operator="eq", values=["ERROR_LOG"])

        parameters.setFilters([filter1])

        request = DescribeLogsRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeLogs()