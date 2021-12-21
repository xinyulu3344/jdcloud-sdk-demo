from jdcloud_sdk.services.monitor.apis.DescribeMetricDataRequest import DescribeMetricDataParameters, \
    DescribeMetricDataRequest
from monitorClient import *

regionId = 'cn-north-1'
metric = 'database.docker.cpu.util'
serviceCode = 'database'
resourceId = 'mysql-ykdunggylk'


def describeMetricData(regionId, metric, serviceCode, resourceId):
    client = getMonitorClient()
    try:
        parameters = DescribeMetricDataParameters(regionId, metric, resourceId)
        parameters.setStartTime("2021-12-03T00:00:00Z")
        parameters.setEndTime("2021-12-03T02:11:59Z")
        parameters.setServiceCode(serviceCode)

        request = DescribeMetricDataRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeMetricData(regionId, metric, serviceCode, resourceId)
