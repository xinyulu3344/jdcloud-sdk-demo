from jdcloud_sdk.services.disk.apis.DescribeSnapshotsRequest import DescribeSnapshotsParameters, \
    DescribeSnapshotsRequest
from diskClient import *


def describeSnapshots():
    client = getDiskClient()
    try:
        parameters = DescribeSnapshotsParameters("cn-north-1")
        request = DescribeSnapshotsRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeSnapshots()
