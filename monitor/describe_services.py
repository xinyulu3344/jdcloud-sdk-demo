from jdcloud_sdk.services.monitor.apis.DescribeServicesRequest import DescribeServicesParameters, DescribeServicesRequest
from monitorClient import *

serviceCode = 'vm'


def describeServices():
    client = getMonitorClient()
    try:
        parameters = DescribeServicesParameters()

        request = DescribeServicesRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeServices()
