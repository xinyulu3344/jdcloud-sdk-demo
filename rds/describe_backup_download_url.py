from jdcloud_sdk.services.rds.apis.DescribeBackupDownloadURLRequest import DescribeBackupDownloadURLParameters, DescribeBackupDownloadURLRequest
from rdsClient import *


def describeBackupDownloadURL():
    client = getRdsClient()

    try:
        parameters = DescribeBackupDownloadURLParameters("cn-north-1", "e02535e7-29ad-4362-ba35-112f762e64c9")

        request = DescribeBackupDownloadURLRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeBackupDownloadURL()
