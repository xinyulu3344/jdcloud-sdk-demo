from jdcloud_sdk.services.cdn.apis.QueryMixStatisticsDataRequest import QueryMixStatisticsDataParameters, \
    QueryMixStatisticsDataRequest
from cdnClient import *


def queryMixStatisticsData():
    client = getCdnClient()
    try:
        parameters = QueryMixStatisticsDataParameters()
        parameters.setStartTime("2020-09-01T10:00:00Z")
        parameters.setEndTime("2020-09-02T10:00:00Z")
        parameters.setPeriod("followTime")

        request = QueryMixStatisticsDataRequest(parameters)

        resp = client.send(request)
        print("requestId: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    queryMixStatisticsData()
