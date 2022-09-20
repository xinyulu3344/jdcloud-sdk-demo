from jdcloud_sdk.services.monitor.apis.DescribeAlarmsRequest import DescribeAlarmsParameters, DescribeAlarmsRequest
from monitorClient import *

serviceCode = ''


def describeAlarms():
    client = getMonitorClient()
    try:
        parameters = DescribeAlarmsParameters()
        parameters.setPageNumber(1)
        parameters.setPageSize(100)
        parameters.setServiceCode(serviceCode)

        request = DescribeAlarmsRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeAlarms()
