#!/usr/bin/python3
from jdcloud_sdk.services.vpc.apis.AssignSecondaryIpsRequest import AssignSecondaryIpsParameters, \
    AssignSecondaryIpsRequest
from vpcClient import *


def assignSecondaryIps():
    client = getVpcClient()
    try:
        parameters = AssignSecondaryIpsParameters("cn-north-1", "port-fr1muoskai")
        # 设置辅ip地址：可以设置多个
        # 参数以列表的形式, ["10.231.6.8", "10.231.6.9"]
        parameters.setSecondaryIps(["192.168.1.172", "192.168.1.173"])
        parameters.setForce(True)

        request = AssignSecondaryIpsRequest(parameters)
        resp = client.send(request)
        print("request_id: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    assignSecondaryIps()
