from jdcloud_sdk.services.cdn.apis.QueryStatisticsDataGroupSumRequest import QueryStatisticsDataGroupSumParameters, \
    QueryStatisticsDataGroupSumRequest
from cdnClient import *


def queryStatisticsDataGroupSum():
    client = getCdnClient()
    try:
        parameters = QueryStatisticsDataGroupSumParameters()
        parameters.setStartTime("2021-10-21T10:00:00Z")
        parameters.setEndTime("2021-10-21T11:00:00Z")
        parameters.setPeriod("oneMin")
        parameters.setGroupBy("domain")

        request = QueryStatisticsDataGroupSumRequest(parameters)

        resp = client.send(request)
        print("requestId: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    queryStatisticsDataGroupSum()
