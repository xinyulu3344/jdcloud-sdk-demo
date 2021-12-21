from jdcloud_sdk.services.vpc.apis.AssociateElasticIpRequest import AssociateElasticIpParameters, \
    AssociateElasticIpRequest
from vpcClient import *


# 给网卡绑公网ip
def associateElasticIp():
    client = getVpcClient()

    try:
        parameters = AssociateElasticIpParameters("cn-north-1", "")
        # 绑定的弹性Ip地址
        parameters.setElasticIpAddress(elasticIpAddress="")
        # 绑定的弹性Ip Id
        parameters.setElasticIpId(elasticIpId="")
        # 绑定弹性Ip到指定的privateIp
        parameters.setPrivateIpAddress(privateIpAddress="")

        request = AssociateElasticIpRequest(parameters)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    associateElasticIp()
