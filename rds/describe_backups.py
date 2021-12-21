from jdcloud_sdk.services.rds.apis.DescribeBackupsRequest import DescribeBackupsParameters, DescribeBackupsRequest
from rdsClient import *


def describeBackups():
    client = getRdsClient()

    try:
        parameters = DescribeBackupsParameters("cn-north-1", "mysql-ykdunggylk", 1, 100)

        request = DescribeBackupsRequest(parameters)
        resp = client.send(request)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeBackups()