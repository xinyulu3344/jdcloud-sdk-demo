from jdcloud_sdk.services.monitor.apis.DescribeMetricsRequest import DescribeMetricsParameters, DescribeMetricsRequest
from monitorClient import *

serviceCode = 'vm'


def describeMetrics(serviceCode):
    client = getMonitorClient()
    try:
        parameters = DescribeMetricsParameters(serviceCode)

        request = DescribeMetricsRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeMetrics(serviceCode)
