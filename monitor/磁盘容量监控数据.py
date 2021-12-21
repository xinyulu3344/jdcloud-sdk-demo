from jdcloud_sdk.services.monitor.apis.DescribeMetricDataRequest import DescribeMetricDataParameters, \
    DescribeMetricDataRequest
from monitorClient import *

regionId = 'cn-north-1'
metric = 'vm.disk.dev.used'
serviceCode = 'vm'
resourceId = 'i-vw11z002j8'


def describeMetricData(regionId, metric, serviceCode, resourceId):
    client = getMonitorClient()
    try:
        parameters = DescribeMetricDataParameters(regionId, metric, resourceId)
        parameters.setTags([{"key": "mountPoint", "values": ["/"]}])
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