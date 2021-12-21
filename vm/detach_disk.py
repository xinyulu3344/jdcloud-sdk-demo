from jdcloud_sdk.services.vm.apis.DetachDiskRequest import DetachDiskParameters, DetachDiskRequest
from vmClient import *


def detachDisk(regionId, instanceId, diskId):
    client = getVmClient()
    try:
        parameters = DetachDiskParameters(regionId, instanceId, diskId)
        request = DetachDiskRequest(parameters)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    detachDisk("cn-north-1", "i-tcqwaf4a0s", "vol-ecv995tj4b")
