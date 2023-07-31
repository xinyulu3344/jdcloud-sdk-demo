from jdcloud_sdk.services.cdn.apis.DomainTxtGenerateRequest import DomainTxtGenerateParameters, DomainTxtGenerateRequest
from cdnClient import *


def domaintxt():
    client = getCdnClient()
    try:
        parameters = DomainTxtGenerateParameters()
        parameters.setDomain("")


        request = DomainTxtGenerateRequest(parameters)

        resp = client.send(request)
        print("requestId: ", resp.request_id)
        if resp.error is not None:
            print(resp.error.code, resp.error.message)
            return
        print(resp.result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    domaintxt()
