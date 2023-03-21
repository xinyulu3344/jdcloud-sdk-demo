from jdcloud_sdk.services.vpc.apis.AddBandwidthPackageIPRequest import AddBandwidthPackageIPParameters, AddBandwidthPackageIPRequest
from jdcloud_sdk.services.vpc.models.AddBandwidthPackageIPSpec import AddBandwidthPackageIPSpec
from vpcClient import *


def addBandwidthPackageIP():
    client = getVpcClient()
    try:
        spec = AddBandwidthPackageIPSpec("fip-xxxx", -1)
        parameter = AddBandwidthPackageIPParameters("cn-east-2", "", [spec])

        request = AddBandwidthPackageIPRequest(parameter)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    addBandwidthPackageIP()