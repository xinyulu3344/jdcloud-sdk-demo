from jdcloud_sdk.services.disk.apis.DescribeDiskRequest import DescribeDiskParameters, \
    DescribeDiskRequest
from diskClient import *


def describeDisk(regionId, diskId):
    client = getDiskClient()
    try:
        parameters = DescribeDiskParameters(regionId, diskId)
        request = DescribeDiskRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeDisk("cn-north-1", "vol-mgu9v6wul9")
