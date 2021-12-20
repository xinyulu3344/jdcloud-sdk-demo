from jdcloud_sdk.services.cdn.apis.GetDomainDetailRequest import GetDomainDetailParameters, GetDomainDetailRequest
from cdnClient import *


def getDomainDetail():
    client = getCdnClient()
    try:
        parameters = GetDomainDetailParameters("")

        request = GetDomainDetailRequest(parameters)

        resp = client.send(request)
        print("requestId: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    getDomainDetail()
