from jdcloud_sdk.services.cdn.apis.QueryRefreshTaskRequest import QueryRefreshTaskParameters, QueryRefreshTaskRequest
from cdnClient import *


def queryRefreshTask():
    client = getCdnClient()
    try:
        parameters = QueryRefreshTaskParameters()
        parameters.setTaskId("6f8b0bba-e0f9-41f5-99d1-d11ef46f1c2a")
        parameters.setStartTime("2021-12-20T00:00:00Z")
        parameters.setEndTime("2021-12-21T00:00:00Z")
        request = QueryRefreshTaskRequest(parameters)

        resp = client.send(request)
        print("requestId: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    queryRefreshTask()
