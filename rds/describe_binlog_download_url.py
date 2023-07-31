from jdcloud_sdk.services.rds.apis.DescribeBinlogDownloadURLRequest import DescribeBinlogDownloadURLParameters, DescribeBinlogDownloadURLRequest
from rdsClient import *

regionId = 'cn-north-1'
instanceId = ''

# 先用describe_binlogs获取 binlogBackupId
binlogBackupId = 'b94f034a-ed57-4dfd-99ed-922fdb01fc62'

# 设置链接地址的过期时间: 1 ~ 86400
seconds = 300



def describeBinlogDownloadURL():
    client = getRdsClient()

    try:
        parameters = DescribeBinlogDownloadURLParameters(regionId, instanceId, binlogBackupId)
        parameters.setSeconds(seconds)

        request = DescribeBinlogDownloadURLRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeBinlogDownloadURL()
