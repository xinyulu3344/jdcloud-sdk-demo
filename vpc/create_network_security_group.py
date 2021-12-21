from jdcloud_sdk.services.vpc.apis.CreateNetworkSecurityGroupRequest import CreateNetworkSecurityGroupParameters, \
    CreateNetworkSecurityGroupRequest
from vpcClient import *


def createNetworkSecurityGroup():
    client = getVpcClient()
    try:
        parameter = CreateNetworkSecurityGroupParameters("cn-north-1", "vpc-nutq6o7xvs", "groupname")
        request = CreateNetworkSecurityGroupRequest(parameter)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    createNetworkSecurityGroup()
