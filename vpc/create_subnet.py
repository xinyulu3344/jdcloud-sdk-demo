from jdcloud_sdk.services.vpc.apis.CreateSubnetRequest import CreateSubnetParameters, CreateSubnetRequest
from vpcClient import *


def createSubnet():
    client = getVpcClient()
    try:
        parameters = CreateSubnetParameters("cn-south-1", "vpc-bz7iir40uo", "sdk_test", "192.168.0.0/24")
        request = CreateSubnetRequest(parameters)
        resp = client.send(request)

        # 打印requestID，调用OpenAPI时会返回requestId，如果调用失败可反馈我们该值
        print("requestId: ", resp.request_id)

        # 错误处理
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return

        print("创建subnet：", resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    createSubnet()
