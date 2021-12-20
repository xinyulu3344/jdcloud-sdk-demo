from jdcloud_sdk.services.cdn.apis.QueryStatisticsDataRequest import QueryStatisticsDataParameters, \
    QueryStatisticsDataRequest
from cdnClient import *


def queryStatisticsData():
    client = getCdnClient()
    try:
        parameters = QueryStatisticsDataParameters()
        parameters.setStartTime("2021-12-16T00:00:00Z")
        parameters.setEndTime("2021-12-17T00:00:00Z")
        parameters.setPeriod("followTime")
        request = QueryStatisticsDataRequest(parameters)

        resp = client.send(request)
        print("requestId: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    queryStatisticsData()
