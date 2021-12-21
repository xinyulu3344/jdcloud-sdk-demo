from jdcloud_sdk.services.rds.apis.DescribeLogDownloadURLRequest import DescribeLogDownloadURLParameters, DescribeLogDownloadURLRequest
from rdsClient import *


def describeLogDownloadURL():
    client = getRdsClient()

    try:
        # 先用describe_logs获取 日志logId
        parameters = DescribeLogDownloadURLParameters("cn-north-1", "mysql-ykdunggylk", "c0c61c7f-30d5-4b5b-9c99-f3dae0ee84b4")

        request = DescribeLogDownloadURLRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeLogDownloadURL()
