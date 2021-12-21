from jdcloud_sdk.services.vm.apis.StartInstanceRequest import StartInstanceParameters, StartInstanceRequest
from vmClient import *


def startInstance(region, instanceId):
    client = getVmClient()
    try:
        parameters = StartInstanceParameters(region, instanceId)
        request = StartInstanceRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    startInstance("cn-east-1", "i-hwxm0olpqh")
