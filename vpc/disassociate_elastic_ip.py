from jdcloud_sdk.services.vpc.apis.DisassociateElasticIpRequest import DisassociateElasticIpParameters, \
    DisassociateElasticIpRequest
from vpcClient import *


# 从网卡解绑公网ip
def disassociateElasticIp():
    client = getVpcClient()
    try:
        parameters = DisassociateElasticIpParameters("cn-north-1", "port-ow2edgq4ad")

        # 指定解绑的弹性Ip Id
        parameters.setElasticIpId("")

        # 指定解绑的弹性Ip地址
        parameters.setElasticIpAddress("")

        request = DisassociateElasticIpRequest(parameters)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    disassociateElasticIp()
