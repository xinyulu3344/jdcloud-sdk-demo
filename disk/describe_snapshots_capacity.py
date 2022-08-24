from jdcloud_sdk.services.disk.apis.DescribeSnapshotsCapacityRequest import DescribeSnapshotsCapacityRequest,DescribeSnapshotsCapacityParameters
from diskClient import *


def describeSnapshotsCapacity(regionId):
    client = getDiskClient()
    try:
        parameters = DescribeSnapshotsCapacityParameters(regionId)
        request = DescribeSnapshotsCapacityRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeSnapshotsCapacity("cn-north-1")