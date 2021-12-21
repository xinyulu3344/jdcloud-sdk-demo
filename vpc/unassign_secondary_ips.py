from jdcloud_sdk.services.vpc.apis.UnassignSecondaryIpsRequest import UnassignSecondaryIpsParameters, \
    UnassignSecondaryIpsRequest
from vpcClient import *


# 给弹性网卡释放地址
def unassignSecondaryIps():
    client = getVpcClient()
    try:
        parameters = UnassignSecondaryIpsParameters("cn-north-1", "port-ow2edgq4ad")
        parameters.setSecondaryIps(["192.168.22.8"])

        request = UnassignSecondaryIpsRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    unassignSecondaryIps()
