from jdcloud_sdk.services.vm.apis.StopInstanceRequest import StopInstanceParameters, StopInstanceRequest
from vmClient import *


def stopInstance(region, instanceId):
    client = getVmClient()
    try:
        parameters = StopInstanceParameters(region, instanceId)
        request = StopInstanceRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    stopInstance("cn-east-1", "i-hwxm0olpqh")
