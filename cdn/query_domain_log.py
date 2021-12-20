from jdcloud_sdk.services.cdn.apis.QueryDomainLogRequest import QueryDomainLogParameters, QueryDomainLogRequest
from cdnClient import *


def queryDomainLog():
    client = getCdnClient()
    try:
        parameters = QueryDomainLogParameters("")
        parameters.setStartTime("2021-12-16T00:00:00Z")
        parameters.setEndTime("2021-12-17T00:00:00Z")

        request = QueryDomainLogRequest(parameters)

        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    queryDomainLog()
