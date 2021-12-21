from jdcloud_sdk.services.vpc.apis.CreateVpcRequest import CreateVpcParameters, CreateVpcRequest
from vpcClient import *


def createVpc():
    client = getVpcClient()

    try:
        parameters = CreateVpcParameters("cn-north-1", "sdk_test")
        parameters.setAddressPrefix("192.168.0.0/16")
        request = CreateVpcRequest(parameters)
        resp = client.send(request)

        print("requestId: ", resp.request_id)

        # 错误处理
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return

        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    createVpc()
