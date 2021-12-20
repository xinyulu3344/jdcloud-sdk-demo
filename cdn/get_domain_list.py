from jdcloud_sdk.services.cdn.apis.GetDomainListRequest import GetDomainListParameters, GetDomainListRequest
from cdnClient import *


def getDomainList():
    client = getCdnClient()
    try:
        parameters = GetDomainListParameters()
        parameters.setAccelerateRegion("mainLand")

        request = GetDomainListRequest(parameters)

        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    getDomainList()
