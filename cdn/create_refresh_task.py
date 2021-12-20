from jdcloud_sdk.services.cdn.apis.CreateRefreshTaskRequest import CreateRefreshTaskParameters,CreateRefreshTaskRequest
from cdnClient import *


def createRefreshTask(urls, taskType):
    client = getCdnClient()
    try:
        parameters = CreateRefreshTaskParameters()
        parameters.setUrls(urls)
        parameters.setTaskType(taskType)
        request = CreateRefreshTaskRequest(parameters)

        resp = client.send(request)
        print("requestId: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    urls = ["URL1", "URL2", "URL3"]
    createRefreshTask(urls, "url")
