from jdcloud_sdk.services.cdn.apis.GetSslCertListRequest import GetSslCertListParameters,GetSslCertListRequest
from cdnClient import *


def getSslCertList():
    client = getCdnClient()
    try:
        parameters = GetSslCertListParameters()
        parameters.setDomain("")
        request = GetSslCertListRequest(parameters)

        resp = client.send(request)
        print(resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    getSslCertList()
