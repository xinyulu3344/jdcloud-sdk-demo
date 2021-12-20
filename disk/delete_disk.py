from jdcloud_sdk.services.disk.apis.DeleteDiskRequest import DeleteDiskParameters,DeleteDiskRequest
from diskClient import *


def deleteDisk(regionId, diskId):
    client = getDiskClient()
    try:
        parameters = DeleteDiskParameters(regionId, diskId)
        request = DeleteDiskRequest(parameters)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    deleteDisk("cn-north-1", "vol-fk82lvo19x")