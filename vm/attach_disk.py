from jdcloud_sdk.services.vm.apis.AttachDiskRequest import AttachDiskParameters, AttachDiskRequest
from vmClient import *


def attachDisk(regionId, instanceId, diskId):
    client = getVmClient()
    try:
        parameters = AttachDiskParameters(regionId, instanceId, diskId)
        request = AttachDiskRequest(parameters)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    attachDisk("cn-north-1", "i-vw11z002j8", "vol-ecv995tj4b")