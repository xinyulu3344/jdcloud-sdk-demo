from jdcloud_sdk.services.vpc.apis.CreateNetworkInterfaceRequest import CreateNetworkInterfaceParameters, \
    CreateNetworkInterfaceRequest
from vpcClient import *


# 创建弹性网卡
def createNetworkInterface():
    # 获取vpc的client
    client = getVpcClient()
    try:
        parameters = CreateNetworkInterfaceParameters("cn-north-1", "subnet-2slgb1fxwb")

        # 设置az
        parameters.setAz("cn-north-1a")

        # 设置网卡名
        parameters.setNetworkInterfaceName("interfacename")

        # 设置描述信息
        parameters.setDescription("")

        # 设置主ip地址
        parameters.setPrimaryIpAddress("192.168.22.100")

        # 源和目标IP地址校验，取值为0或者1,默认为1
        parameters.setSanityCheck(0)

        # 自动分配的SecondaryIp数量
        # parameters.setSecondaryIpCount(1)

        # 要绑定的安全组ID列表，最多指定5个安全组
        parameters.setSecurityGroups(["sg-kmtuwys23r"])

        # SecondaryIp列表
        parameters.setSecondaryIpAddresses(["192.168.22.101", "192.168.22.102"])

        request = CreateNetworkInterfaceRequest(parameters)
        resp = client.send(request)

        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    createNetworkInterface()
