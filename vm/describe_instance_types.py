from jdcloud_sdk.services.vm.apis.DescribeInstanceTypesRequest import DescribeInstanceTypesParameters,DescribeInstanceTypesRequest
from jdcloud_sdk.services.common.models.Filter import Filter
from vmClient import *


def describeInstanceTypes():
    client = getVmClient()

    try:
        parameters = DescribeInstanceTypesParameters("cn-north-1")
        # filter1 = Filter(name="_offline", values=[], operator="eq")
        # filter2 = Filter(name="instanceTypes", values=["g.s1.small"], operator="eq")
        # parameters.setFilters([filter1, filter2])
        request = DescribeInstanceTypesRequest(parameters)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            print(resp.request_id)
            return
        print(resp.result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeInstanceTypes()
