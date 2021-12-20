from jdcloud_sdk.services.cdn.apis.SetHttpTypeRequest import SetHttpTypeParameters,SetHttpTypeRequest
from cdnClient import *


def setHttpType():
    client = getCdnClient()
    try:
        parameters = SetHttpTypeParameters("")
        parameters.setHttpType("http")
        request = SetHttpTypeRequest(parameters)
        resp = client.send(request)
        print("requestId: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        result = resp.result
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    setHttpType()
