import os
import requests
from urllib.parse import urlparse
from jdcloud_sdk.services.rds.client.RdsClient import RdsClient
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.core.logger import Logger
from jdcloud_sdk.core.logger import ERROR
from jdcloud_sdk.core.config import Config
from jdcloud_sdk.core.const import SCHEME_HTTPS
from jdcloud_sdk.services.rds.apis.DescribeBinlogsRequest import DescribeBinlogsParameters,DescribeBinlogsRequest
from jdcloud_sdk.services.rds.apis.DescribeBinlogDownloadURLRequest import DescribeBinlogDownloadURLParameters, DescribeBinlogDownloadURLRequest

accessKey = ''
secretKey = ''
endpoint = 'rds.jdcloud-api.com'
regionId = 'cn-north-1'
instanceId = ''
startTime = '2023-07-31 00:00:00'
endTime = '2023-07-31 02:00:00'
seconds = 300
pageSize = 100

# 公网下载: publicURL
# 内网下载: internalURL
network = "publicURL"
outdir = '.\mybinlog'


def getRdsClient():
    credential = Credential(access_key=accessKey, secret_key=secretKey)
    config = Config(endpoint='rds.jdcloud-api.com', scheme=SCHEME_HTTPS, timeout=10)
    client = RdsClient(credential=credential, config=config, logger=Logger(ERROR))
    return client


client = getRdsClient()


def describeBinlogs(pageNumber):
    binlogInfos = {}
    try:
        parameters = DescribeBinlogsParameters(regionId, instanceId)
        parameters.setPageNumber(pageNumber)
        parameters.setPageSize(pageSize)
        parameters.setStartTime(startTime)
        parameters.setEndTime(endTime)

        request = DescribeBinlogsRequest(parameters)
        resp = client.send(request)
        print("describeBinlogs requestId: ", resp.request_id)
        if resp.error is not None:
            print("describeBinlogs error: ", resp.error.code, resp.error.message)
            return binlogInfos
        for binlog in resp.result['binlogs']:
            binlogInfos[binlog['binlogBackupId']] = binlog
        return binlogInfos
    except Exception as e:
        print(e)


def describeBinlogDownloadURL(binlogBackupId):

    try:
        parameters = DescribeBinlogDownloadURLParameters(regionId, instanceId, binlogBackupId)
        parameters.setSeconds(seconds)

        request = DescribeBinlogDownloadURLRequest(parameters)
        resp = client.send(request)
        print("describeBinlogDownloadURL requestId: ", resp.request_id)
        if resp.error is not None:
            print("describeBinlogDownloadURL error: ", resp.error.code, resp.error.message)
            return
        return resp.result
    except Exception as e:
        print(e)


def getTotal():
    try:
        parameters = DescribeBinlogsParameters(regionId, instanceId)
        parameters.setPageNumber(1)
        parameters.setPageSize(10)
        parameters.setStartTime(startTime)
        parameters.setEndTime(endTime)

        request = DescribeBinlogsRequest(parameters)
        resp = client.send(request)
        print("getTotal describeBinlogs requestId: ", resp.request_id)
        if resp.error is not None:
            print("getTotal describeBinlogs error: ", resp.error.code, resp.error.message)
            return -1
        return resp.result['totalCount']
    except Exception as e:
        print(e)


def main():
    totalCount = getTotal()
    if totalCount < 0:
        return
    loopCount = (totalCount + pageSize - 1) // pageSize
    for i in range(1, loopCount+1):
        binlogInfos = describeBinlogs(i)
        for binlogId, binlogInfo in binlogInfos.items():
            url = describeBinlogDownloadURL(binlogId)
            parsed_url = urlparse(url[network])
            filename = os.path.basename(parsed_url.path)
            file = requests.get(url[network])
            with open(os.path.join(outdir, filename), 'wb') as f:
                f.write(file.content)


if __name__ == "__main__":
    main()