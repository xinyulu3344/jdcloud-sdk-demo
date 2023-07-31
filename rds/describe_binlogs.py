from jdcloud_sdk.services.rds.apis.DescribeBinlogsRequest import DescribeBinlogsParameters,DescribeBinlogsRequest
from rdsClient import *

regionId = 'cn-north-1'
instanceId = ""
pageNumber = 1
pageSize = 100
startTime = '2023-07-31 00:00:00'
endTime = "2023-07-31 10:00:00"


def describeBinlogs():
    client = getRdsClient()

    try:
        parameters = DescribeBinlogsParameters(regionId, instanceId)
        parameters.setPageNumber(pageNumber)
        parameters.setPageSize(pageSize)
        parameters.setStartTime(startTime)
        parameters.setEndTime(endTime)

        request = DescribeBinlogsRequest(parameters)
        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    describeBinlogs()